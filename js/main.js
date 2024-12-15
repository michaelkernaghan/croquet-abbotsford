// Add smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        // Handle contact link specially
        if (this.getAttribute('href') === 'contact') {
            e.preventDefault();
            window.location.href = 'contact.html';
            return;
        }
        // Only prevent default and do smooth scroll for other hash links
        if (this.getAttribute('href').startsWith('#')) {
            e.preventDefault();
            const section = document.querySelector(this.getAttribute('href'));
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});