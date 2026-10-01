const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const manifest = require('./public-files.json');
const consent = fs.readFileSync(path.join(root, 'assets/js/consent.js'), 'utf8');

function consentContext(saved, failStorage = false) {
  const scripts = [];
  const flags = new Set();
  const context = {
    window: {},
    localStorage: {
      getItem() { if (failStorage) throw Error('blocked'); return saved === undefined ? null : JSON.stringify(saved); },
      removeItem() {}
    },
    document: {
      readyState: 'loading', addEventListener() {},
      getElementById(id) { return scripts.find(script => script.id === id); },
      createElement() { return {}; }, head: { appendChild(script) { scripts.push(script); } },
      documentElement: { hasAttribute(name) { return flags.has(name); }, setAttribute(name) { flags.add(name); } }
    }
  };
  vm.runInNewContext(consent, context);
  return { scripts, calls: context.window.dataLayer.map(entry => Array.from(entry)), window: context.window };
}
function saved(analytics, marketing) { return { version: 2, analytics, marketing, time: Date.now() - 1000 }; }
test('new, expired, invalid and blocked-storage visits load no optional tag', () => {
  for (const value of [undefined, { ...saved(true, true), time: 0 }, { ...saved(true, true), time: Date.now() + 100000 }, { version: 2, analytics: 'yes', marketing: true, time: Date.now() }]) {
    const result = consentContext(value);
    assert.equal(result.scripts.length, 0);
    assert.deepEqual(result.calls[0].slice(0, 2), ['consent', 'default']);
    for (const field of ['analytics_storage', 'ad_storage', 'ad_user_data', 'ad_personalization']) assert.equal(result.calls[0][2][field], 'denied');
  }
  assert.equal(consentContext(saved(true, true), true).scripts.length, 0);
});
test('refusal persists without optional tags', () => { assert.equal(consentContext(saved(false, false)).scripts.length, 0); });
test('analytics-only loads GA without Ads or Meta', () => {
  const result = consentContext(saved(true, false));
  assert.equal(result.scripts.length, 1);
  assert.match(result.scripts[0].src, /G-V9BGEJKQKZ$/);
  assert.ok(result.calls.some(call => call[0] === 'config' && call[1] === 'G-V9BGEJKQKZ'));
  assert.ok(!result.calls.some(call => call[0] === 'config' && call[1].startsWith('AW-')));
  assert.equal(result.window.fbq, undefined);
});
test('marketing-only loads Ads and Meta without GA configuration', () => {
  const result = consentContext(saved(false, true));
  assert.equal(result.scripts.length, 2);
  assert.ok(result.calls.some(call => call[0] === 'config' && call[1] === 'AW-17462997481'));
  assert.ok(!result.calls.some(call => call[0] === 'config' && call[1] === 'G-V9BGEJKQKZ'));
  assert.equal(result.window.fbq.queue.length, 3);
});

function simulatorContext() {
  let source = fs.readFileSync(path.join(root, 'assets/js/etude-gratuite-simulateur.js'), 'utf8');
  source = source.replace('window.initEtudeGratuiteSimulateur = initEtudeGratuiteSimulateur;', 'window.test = { computeEstimation, updateIllustration, setRoot(value) { root = value; } };');
  const context = { window: {}, document: { readyState: 'loading', addEventListener() {} }, console };
  vm.runInNewContext(source, context); return context.window.test;
}
test('a horizontal roof keeps 0 degrees instead of becoming 30 degrees', () => {
  const simulator = simulatorContext();
  const input = { surface: 30, orientation: 'sud', obstacles: 'non' };
  assert.equal(simulator.computeEstimation({ ...input, inclinaison: 0 }).production, 5000);
  assert.equal(simulator.computeEstimation({ ...input, inclinaison: 30 }).production, 6600);
});
test('video load returning void never breaks navigation; rejected playback shows fallback', async () => {
  const simulator = simulatorContext(); const fallback = { style: {} };
  const video = { style: {}, load() {}, play() { return Promise.reject(Error('autoplay')); } };
  simulator.setRoot({ querySelector(selector) { return selector === '#etude-sim-video' ? video : fallback; } });
  assert.doesNotThrow(() => simulator.updateIllustration(0));
  await Promise.resolve(); assert.equal(fallback.style.display, 'flex'); assert.equal(video.style.display, 'none');
});
test('the public build contains only approved PDFs and excludes working documents', () => {
  const files = [];
  function walk(dir) { for (const entry of fs.readdirSync(dir, { withFileTypes: true })) { const full = path.join(dir, entry.name); if (entry.isDirectory()) walk(full); else files.push(path.relative(path.join(root, 'dist'), full).replaceAll('\\', '/')); } }
  walk(path.join(root, 'dist'));
  assert.deepEqual(files.filter(file => file.endsWith('.pdf')).sort(), manifest.pdfs.slice().sort());
  assert.ok(!files.some(file => /\.(md|docx|py|toml)$|^(scripts|tmp|docs|output)\/|FredericFRANCOIS/i.test(file)));
  for (const file of manifest.pages) {
    const html = fs.readFileSync(path.join(root, 'dist', file), 'utf8');
    assert.ok(!html.includes('googletagmanager.com/gtm.js') && !html.includes('googletagmanager.com/ns.html'), file);
    if (html.includes('<head') && !/http-equiv="refresh"/i.test(html) && !file.startsWith('google')) assert.equal((html.match(/src="\/assets\/js\/consent.js"/g) || []).length, 1, file);
  }
});
test('the removed document route returns 410 and forbids caching/indexing', () => {
  let source = fs.readFileSync(path.join(root, 'api/gone-document.js'), 'utf8').replace('export default function', 'function');
  const headers = {}; const response = { setHeader(name, value) { headers[name] = value; }, status(code) { this.code = code; return this; }, send(body) { this.body = body; } };
  vm.runInNewContext(source + '\nhandler({}, response);', { response });
  assert.equal(response.code, 410); assert.equal(headers['Cache-Control'], 'no-store'); assert.match(headers['X-Robots-Tag'], /noindex/);
});
