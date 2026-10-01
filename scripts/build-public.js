const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const output = path.resolve(root, 'dist');
const manifest = require('./public-files.json');
const pdfs = new Set(manifest.pdfs);
const mediaExtensions = new Set(['.css', '.js', '.png', '.jpg', '.jpeg', '.webp', '.avif', '.svg', '.gif', '.ico', '.mp4', '.webm', '.woff', '.woff2', '.ttf', '.otf']);
// Only this exact generated directory may be replaced; never publish the repo.
if (output !== path.join(root, 'dist')) throw new Error('Invalid output path');
fs.rmSync(output, { recursive: true, force: true });
fs.mkdirSync(output, { recursive: true });
let count = 0;
function copy(relative) {
  const source = path.resolve(root, relative);
  if (!source.startsWith(root + path.sep) || fs.lstatSync(source).isSymbolicLink()) throw new Error('Unsafe public path: ' + relative);
  const destination = path.join(output, relative);
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.copyFileSync(source, destination); count++;
}
function assets(directory) {
  for (const entry of fs.readdirSync(path.join(root, directory), { withFileTypes: true })) {
    if (entry.name.startsWith('.') || entry.isSymbolicLink()) continue;
    const relative = directory + '/' + entry.name;
    if (entry.isDirectory()) assets(relative);
    else {
      const extension = path.extname(entry.name).toLowerCase();
      if (extension === '.pdf' && !pdfs.has(relative)) throw new Error('PDF not approved for publication: ' + relative);
      if (mediaExtensions.has(extension) || pdfs.has(relative)) copy(relative);
    }
  }
}
manifest.pages.forEach(copy);
['components/header.html', 'components/footer.html', 'robots.txt', 'sitemap.xml', '_redirects', '.htaccess'].forEach(copy);
assets('assets');
console.log(`Public build: ${count} files; ${manifest.pages.length} pages; ${pdfs.size} approved manufacturer PDFs.`);
