/* Service Worker für das Familien-WM-Tippspiel 2026.
   Macht die App offline-fähig (App-Shell-Caching) und installierbar.
   Aktiv nur, wenn die Seite über http(s) ausgeliefert wird. */
const CACHE = "wm-tippspiel-v79";
const ASSETS = [
  "./",
  "./wm-tippspiel.html",
  "./anleitung.html",
  "./manifest.json",
  "./icon.svg",
  "./cloud-config.js"
];

// Installation: App-Shell in den Cache legen (einzeln, damit ein fehlendes
// Asset die Installation nicht komplett scheitern lässt).
self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => Promise.allSettled(ASSETS.map((a) => c.add(a))))
      .then(() => self.skipWaiting())
  );
});

// Aktivierung: alte Cache-Versionen aufräumen.
self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Abruf: erst Cache, sonst Netz – und neue Treffer gleicher Herkunft nachcachen.
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request).then((hit) =>
      hit || fetch(e.request).then((resp) => {
        const copy = resp.clone();
        try {
          if (resp.ok && new URL(e.request.url).origin === location.origin) {
            caches.open(CACHE).then((c) => c.put(e.request, copy));
          }
        } catch (_) { /* ungültige URL ignorieren */ }
        return resp;
      }).catch(() => caches.match("./wm-tippspiel.html"))
    )
  );
});
