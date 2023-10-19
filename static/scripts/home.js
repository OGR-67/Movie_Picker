document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            console.log(entry);
            if (entry.isIntersecting) {
                const image = entry.target;
                const src = image.getAttribute('data-src');
                if (src) {
                    image.src = src;
                    observer.unobserve(image);
                }
            }
        });
    });

    const lazyImages = document.querySelectorAll('img[data-src]');

    lazyImages.forEach((img) => {
        observer.observe(img);
    });
});