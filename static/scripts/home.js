document.addEventListener('DOMContentLoaded', () => {
    // Add event listeners to all movie details buttons
    const generic_movie_detail_url = document.querySelector(".home-datas").dataset.generic_movie_detail_url;

    document.querySelectorAll('.movie-card__details-btn').forEach(button => {
        button.addEventListener('click', () => {
            const movieId = +button.getAttribute("data-movie-id");
            window.location.href = generic_movie_detail_url.replace('0', movieId);
        });
    });

    // Add event listener to filters title
    document.querySelector(".filters-title").addEventListener("click", (event) => {
        event.preventDefault();
        document.querySelector(".filters-section").classList.toggle("hidden");
        document.querySelector(".arrow").classList.toggle("rotate");
    });

    // Convert movies rating values to stars
    document.querySelectorAll(".movie-card__rating").forEach(rating => {
        convertRatingToStars(rating);
    });

    // min rating filter input converted to selectable stars
    currentRatingFilter = +document.querySelector("input[type=hidden]").value || 0;
    ratingFilterStars = currentRatingFilter / 2 + 1;
    document.querySelectorAll(".rating-star").forEach(star => {
        if (star.getAttribute("data-rating") <= ratingFilterStars) {
            star.innerHTML = starFull;
        }
    });

    // Add event listeners to all rating stars
    document.querySelectorAll(".rating-star").forEach(star => {
        star.addEventListener("click", (event) => {
            event.preventDefault();
            const rating = star.getAttribute("data-rating");
            document.querySelectorAll(".rating-star").forEach(star => {
                star.getAttribute("data-rating") <= rating
                    ? star.innerHTML = starFull
                    : star.innerHTML = starOutline;
            });
            document.querySelector("input[type=hidden]").value = (rating * 2) - 2;
        });
    });

    // Lazy load images
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
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

