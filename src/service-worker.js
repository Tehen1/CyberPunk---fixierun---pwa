const CACHE_NAME = 'fixie-v1';
const ASSETS = ['/', '/index.html', '/src/css/styles.css', '/manifest.json'];

self.addEventListener('install', (event) => {
    console.log('Installing service worker...');
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Caching assets...');
                return cache.addAll(ASSETS);
            })
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') {
        return;
    }
    
    console.log('Handling fetch event for:', event.request.url);
    
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                if (response) {
                    console.log('Serving from cache:', response.url);
                    return response;
                }
                console.log('Fetching from network:', event.request.url);
                return fetch(event.request)
                    .then((networkResponse) => {
                        if (!networkResponse.ok) {
                            throw new Error('Network response was not ok');
                        }
                        console.log('Caching new resource:', event.request.url);
                        return caches.open(CACHE_NAME)
                            .then((cache) => {
                                return cache.put(event.request, networkResponse.clone());
                            });
                        return networkResponse;
                    })
                    .catch((error) => {
                        console.error('Fetch failed:', error);
                        throw error;
                    });
            })
            .catch((error) => {
                console.error('Service worker fetch error:', error);
                throw error;
            })
    );
});
