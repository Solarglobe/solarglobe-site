const fs = require("fs");
const path = require("path");

const root = process.cwd();
const ignored = new Set(["node_modules", ".git", "output", "tmp"]);
const forbidden = [
  /guide-parcours-solarglobe\.pdf/i,
  /Pose par nos équipes/i,
  /nos équipes certifiées/i,
  /notre garantie décennale/i,
  /SolarGlobe installateur RGE/i,
  /Solarglobe installateur RGE/i,
  /plus qu[’']un installateur/i,
  /jusqu[’']?à 90\s?% de votre facture/i,
  /jusqu[’']?a 90\s?% de votre facture/i,
  /nous pilotons l[’']exécution/i,
  /pas uniquement installateur/i,
  /projet piloté jusqu[’']?à la mise en service/i,
  /projet encadré par SolarGlobe/i,
  /Pose encadrée/i,
  /SolarEnergyContractor/i,
  /SolarGlobe étudie, sélectionne et pilote/i,
  /SolarGlobe assure la cohérence technique entre étude et exécution/i,
  /Un installateur RGE QualiPV ; SolarGlobe assure la cohérence avec l[’']étude/i,
  /cohérence entre le dossier technique, la pose et la mise en service/i,
  /Nous vérifions votre toiture/i,
  /nous vérifions votre toiture/i,
  /plan de pose/i,
  /Cette étape fixe la production attendue/i,
  /médiateur de la consommation sera communiqué/i,
  /dès sa désignation/i,
  /30 000 euros/i,
  /25\/06\/2026/i,
  /16\/04\/2026/i,
  /© 2025/i,
  /18 mars 2025/i,
];
const exts = new Set([".html", ".js", ".json", ".xml", ".txt"]);
const hits = [];
const allowedExactFiles = new Set([
  "scripts\\check-public-compliance.js",
  "scripts/check-public-compliance.js",
  "vercel.json",
]);

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (ignored.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full);
    } else if (exts.has(path.extname(entry.name).toLowerCase())) {
      const relative = path.relative(root, full);
      if (allowedExactFiles.has(relative)) continue;
      const text = fs.readFileSync(full, "utf8");
      for (const rx of forbidden) {
        if (rx.test(text)) hits.push(`${relative} :: ${rx}`);
      }
    }
  }
}

walk(root);
if (fs.existsSync(path.join(root, "assets", "guide-parcours-solarglobe.pdf"))) {
  hits.push("assets/guide-parcours-solarglobe.pdf still exists");
}

if (hits.length) {
  console.error(hits.join("\n"));
  process.exit(1);
}

console.log("public compliance checks passed");
