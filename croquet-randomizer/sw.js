// Offline shell for the roller.
//
// A browser installs a new worker only when THIS FILE's bytes change. Relying on a
// human to bump a version string failed twice on 2026-08-29: two deploys shipped a
// byte-identical worker, no new install fired, and installed phones kept serving the
// first version they ever cached. The club build now derives CACHE from a hash of the
// built page (build.js), so a changed app always means a changed worker.
const CACHE = 'croquet-randomizer-club-b98cd2410cb0';

// The printable pocket card is deliberately absent: it was retired when the app
// replaced the dice, and test/pwa.test.js asserts nothing shipped still links it.
const CACHE_FILES = [
  './',
  './index.html',
  './manifest.json'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE)
    .then(c => c.addAll(CACHE_FILES))
    .then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

// Stale-while-revalidate: hand back the cached copy at once, so the app opens instantly
// and works with no signal on a lawn, then refresh the cache in the background so the
// next launch is current. Plain cache-first never revalidated, which is what froze
// phones on the version they first installed.
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(cached => {
    const fresh = fetch(e.request).then(res => {
      if (res && res.ok) caches.open(CACHE).then(c => c.put(e.request, res.clone()));
      return res;
    }).catch(() => cached);
    return cached || fresh;
  }));
});
