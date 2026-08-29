// Offline shell for the roller. Bump CACHE on every shipped change, or a phone
// that already installed the app keeps serving the previous version forever.
const CACHE = 'croquet-randomizer-club-v1';

// The printable pocket card is deliberately absent: it was retired when the app
// replaced the dice, and test/pwa.test.js asserts nothing shipped still links it.
const CACHE_FILES = [
  './',
  './index.html',
  './manifest.json'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CACHE_FILES)));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))));
});

self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
