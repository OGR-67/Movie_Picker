document.addEventListener("DOMContentLoaded", function () {
    const add_to_watchlist_base_url = document.querySelector(".watchlist-datas").getAttribute("data-add-url");
    const remove_from_watchlist_base_url = document.querySelector(".watchlist-datas").getAttribute("data-remove-url");
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
        button.addEventListener("mouseover", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-solid fa-eye-slash");
        });
        button.addEventListener("mouseout", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-solid fa-eye");

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
        button.addEventListener("mouseover", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-solid fa-plus");
        });
        button.addEventListener("mouseout", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-regular fa-eye");
        });
    });
});