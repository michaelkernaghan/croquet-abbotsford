// Sample configuration file for API keys and other sensitive data
// For production: 
// 1. Copy this file to config.js
// 2. Add your actual API keys
// 3. Make sure config.js is in your .gitignore

const config = {
    // OpenWeatherMap API key
    weatherApiKey: "YOUR_API_KEY_HERE",
    
    // Abbotsford coordinates
    location: {
        lat: 49.0504,
        lon: -122.3045
    }
};

// Make config available globally
if (typeof window !== 'undefined') {
    window.siteConfig = config;
} 