export default function handler(req, res) {
  res.setHeader("X-Robots-Tag", "noindex, noarchive, nosnippet");
  res.setHeader("Cache-Control", "public, max-age=0, must-revalidate");
  res
    .status(410)
    .send(`<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="robots" content="noindex, noarchive, nosnippet"><title>Document supprime | SolarGlobe</title></head><body><main style="font-family:Arial,sans-serif;max-width:720px;margin:48px auto;line-height:1.5"><h1>Document supprime</h1><p>Ce guide est retire car il ne correspond plus au modele contractuel actuel de SolarGlobe.</p><p><a href="/qui-fait-quoi/">Comprendre qui fait quoi chez SolarGlobe</a></p></main></body></html>`);
}
