document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".remove-watchlist").forEach((button) => {
        button.addEventListener("click", () => {
            const movieId = +button.getAttribute("data-movie-id");

            fetch(`${remove_from_watchlist_base_url}?movie_id=${movieId}`)
                .then(function (response) {
                    if (response.status === 200) {
                        window.location.reload();
                    }
                });
        });
    });

    document.querySelectorAll(".add-watchlist").forEach((button) => {
        button.addEventListener("click", () => {
            const movieId = +button.getAttribute("data-movie-id");
            fetch(`${add_to_watchlist_base_url}?movie_id=${movieId}`)
                .then(function (response) {
                    if (response.status === 200) {
                        window.location.reload();
                    }
                });
        });
    });
});