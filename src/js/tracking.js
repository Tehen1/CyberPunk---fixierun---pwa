class Tracker {
    constructor() {
        this.initialize();
    }

    initialize() {
        this.pageViews = 0;
        this.events = [];
        this.registerEvents();
    }

    registerEvents() {
        window.addEventListener('pageview', (event) => this.trackPageView(event));
        window.addEventListener('click', (event) => this.trackClick(event));
    }

    trackPageView(event) {
        this.pageViews++;
        console.log(`Page view #${this.pageViews}`);
        this.sendAnalytics('page_view', {
            page: window.location.pathname,
            timestamp: new Date().toISOString()
        });
    }

    trackClick(event) {
        const target = event.target;
        if (target && target.tagName === 'BUTTON') {
            console.log('Button click tracked:', target.textContent);
            this.sendAnalytics('click', {
                action: 'button_click',
                button_text: target.textContent,
                timestamp: new Date().toISOString()
            });
        }
    }

    sendAnalytics(type, data) {
        // TODO: Implement actual analytics sending
        console.log('Analytics data:', { type, data });
    }
}

// Initialize tracker
const tracker = new Tracker();