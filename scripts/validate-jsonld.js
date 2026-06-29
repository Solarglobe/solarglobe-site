const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const ignoredDirs = new Set([".git", "node_modules"]);
const scriptRe =
  /<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;

function walk(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (ignoredDirs.has(entry.name)) continue;
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) files.push(...walk(fullPath));
    if (entry.isFile() && entry.name.endsWith(".html")) files.push(fullPath);
  }
  return files;
}

function typeName(value) {
  if (Array.isArray(value)) return "array";
  if (value === null) return "null";
  return typeof value;
}

function isAbsoluteUrl(value) {
  return typeof value === "string" && /^https?:\/\//i.test(value);
}

function hasType(node, schemaType) {
  const type = node && node["@type"];
  return type === schemaType || (Array.isArray(type) && type.includes(schemaType));
}

function pathLabel(file, scriptIndex, jsonPath) {
  return `${path.relative(root, file)} script #${scriptIndex} ${jsonPath}`;
}

function addIssue(issues, file, scriptIndex, jsonPath, message) {
  issues.push(`${pathLabel(file, scriptIndex, jsonPath)}: ${message}`);
}

function validateUrlField(issues, file, scriptIndex, jsonPath, value) {
  if (typeof value === "string") {
    if (!isAbsoluteUrl(value)) {
      addIssue(issues, file, scriptIndex, jsonPath, "URL absolue attendue");
    }
    return;
  }

  if (Array.isArray(value)) {
    value.forEach((item, index) =>
      validateUrlField(issues, file, scriptIndex, `${jsonPath}[${index}]`, item),
    );
    return;
  }

  if (value && typeof value === "object") {
    if (value.url !== undefined) {
      validateUrlField(issues, file, scriptIndex, `${jsonPath}.url`, value.url);
    }
    return;
  }

  addIssue(
    issues,
    file,
    scriptIndex,
    jsonPath,
    `URL string ou ImageObject attendu, reçu ${typeName(value)}`,
  );
}

function validateAreaServed(issues, file, scriptIndex, jsonPath, value) {
  if (typeof value === "string") return;
  if (value && typeof value === "object" && !Array.isArray(value)) {
    if (typeof value["@type"] !== "string" || typeof value.name !== "string") {
      addIssue(
        issues,
        file,
        scriptIndex,
        jsonPath,
        "areaServed objet attendu avec @type et name strings",
      );
    }
    return;
  }

  addIssue(
    issues,
    file,
    scriptIndex,
    jsonPath,
    `areaServed doit etre une string ou un objet propre, reçu ${typeName(value)}`,
  );
}

function validateOpeningHours(issues, file, scriptIndex, jsonPath, value) {
  const specs = Array.isArray(value) ? value : [value];
  specs.forEach((spec, index) => {
    const base = `${jsonPath}[${index}]`;
    if (!spec || typeof spec !== "object" || spec["@type"] !== "OpeningHoursSpecification") {
      addIssue(issues, file, scriptIndex, base, "OpeningHoursSpecification attendu");
      return;
    }
    if (!(typeof spec.dayOfWeek === "string" || Array.isArray(spec.dayOfWeek))) {
      addIssue(issues, file, scriptIndex, `${base}.dayOfWeek`, "string ou array attendu");
    }
    if (typeof spec.opens !== "string" || !/^\d{2}:\d{2}$/.test(spec.opens)) {
      addIssue(issues, file, scriptIndex, `${base}.opens`, "heure HH:MM attendue");
    }
    if (typeof spec.closes !== "string" || !/^\d{2}:\d{2}$/.test(spec.closes)) {
      addIssue(issues, file, scriptIndex, `${base}.closes`, "heure HH:MM attendue");
    }
  });
}

function validateBreadcrumb(issues, file, scriptIndex, node, jsonPath) {
  if (!hasType(node, "BreadcrumbList")) return;
  if (!Array.isArray(node.itemListElement)) {
    addIssue(issues, file, scriptIndex, `${jsonPath}.itemListElement`, "array attendu");
    return;
  }

  node.itemListElement.forEach((item, index) => {
    const base = `${jsonPath}.itemListElement[${index}]`;
    if (!item || typeof item !== "object" || item["@type"] !== "ListItem") {
      addIssue(issues, file, scriptIndex, base, "ListItem attendu");
      return;
    }
    if (typeof item.position !== "number") {
      addIssue(issues, file, scriptIndex, `${base}.position`, "number attendu");
    }
    if (typeof item.name !== "string" || item.name.trim() === "") {
      addIssue(issues, file, scriptIndex, `${base}.name`, "string non vide attendue");
    }
    if (item.item !== undefined && !isAbsoluteUrl(item.item)) {
      addIssue(issues, file, scriptIndex, `${base}.item`, "URL absolue attendue");
    }
  });
}

function validateValue(issues, file, scriptIndex, value, jsonPath = "$") {
  if (!value || typeof value !== "object") return;
  if (Array.isArray(value)) {
    value.forEach((item, index) =>
      validateValue(issues, file, scriptIndex, item, `${jsonPath}[${index}]`),
    );
    return;
  }

  validateBreadcrumb(issues, file, scriptIndex, value, jsonPath);

  for (const [key, child] of Object.entries(value)) {
    const childPath = `${jsonPath}.${key}`;

    if (["telephone", "priceRange", "postalCode"].includes(key) && typeof child !== "string") {
      addIssue(
        issues,
        file,
        scriptIndex,
        childPath,
        `string attendue, reçu ${typeName(child)}`,
      );
    }

    if (key === "address") {
      if (!child || typeof child !== "object" || Array.isArray(child) || child["@type"] !== "PostalAddress") {
        addIssue(issues, file, scriptIndex, childPath, "PostalAddress objet attendu");
      }
    }

    if (key === "geo") {
      if (!child || typeof child !== "object" || Array.isArray(child) || child["@type"] !== "GeoCoordinates") {
        addIssue(issues, file, scriptIndex, childPath, "GeoCoordinates objet attendu");
      }
    }

    if (key === "areaServed") {
      validateAreaServed(issues, file, scriptIndex, childPath, child);
    }

    if (key === "price") {
      const validNumber = typeof child === "number" && Number.isFinite(child);
      const validString = typeof child === "string" && /^\d+(\.\d+)?$/.test(child);
      if (!validNumber && !validString) {
        addIssue(issues, file, scriptIndex, childPath, "nombre ou string numerique attendu");
      }
    }

    if (key === "priceCurrency" && child !== "EUR") {
      addIssue(issues, file, scriptIndex, childPath, '"EUR" attendu');
    }

    if (["url", "image", "logo"].includes(key)) {
      validateUrlField(issues, file, scriptIndex, childPath, child);
    }

    if (key === "openingHoursSpecification") {
      validateOpeningHours(issues, file, scriptIndex, childPath, child);
    }

    validateValue(issues, file, scriptIndex, child, childPath);
  }
}

function main() {
  const issues = [];
  let count = 0;

  for (const file of walk(root)) {
    const html = fs.readFileSync(file, "utf8");
    let match;
    let scriptIndex = 0;
    scriptRe.lastIndex = 0;

    while ((match = scriptRe.exec(html))) {
      scriptIndex += 1;
      count += 1;
      const raw = match[1].trim();
      try {
        const data = JSON.parse(raw);
        validateValue(issues, file, scriptIndex, data);
      } catch (error) {
        addIssue(issues, file, scriptIndex, "JSON.parse", error.message);
      }
    }
  }

  if (issues.length > 0) {
    console.error(`JSON-LD invalide: ${issues.length} probleme(s) trouve(s).`);
    for (const issue of issues) console.error(`- ${issue}`);
    process.exit(1);
  }

  console.log(`JSON-LD OK: ${count} script(s) verifies.`);
}

main();
