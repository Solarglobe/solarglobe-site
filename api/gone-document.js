export default function handler(req, res) {
  res.setHeader('X-Robots-Tag', 'noindex, noarchive, nosnippet');
  res.setHeader('Cache-Control', 'no-store');
  res.status(410).send('<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="robots" content="noindex, noarchive, nosnippet"><title>Document retiré | SolarGlobe</title><main><h1>Document retiré</h1><p>Ce document n’est plus disponible.</p><a href="/">Accueil SolarGlobe</a></main></html>');
}
