document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".remove-favorite").forEach((button) => {
        button.addEventListener("click", () => {
            const movieId = +button.getAttribute("data-movie-id");

            fetch(`${remove_from_fav_base_url}?movie_id=${movieId}`)
                .then(function (response) {
                    if (response.status === 200) {
                        window.location.reload();
                    }
                });
        });
        button.addEventListener("mouseover", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-solid fa-heart-circle-xmark");
        });
        button.addEventListener("mouseout", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-solid fa-heart");
        });
    });

    document.querySelectorAll(".add-favorite").forEach((button) => {
        button.addEventListener("click", () => {
            const movieId = +button.getAttribute("data-movie-id");
            fetch(`${add_to_fav_base_url}?movie_id=${movieId}`)
                .then(function (response) {
                    if (response.status === 200) {
                        window.location.reload();
                    }
                });
        });
        button.addEventListener("mouseover", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-solid fa-heart-circle-plus");
        });
        button.addEventListener("mouseout", () => {
            const icon = button.firstChild;
            icon.setAttribute("class", "fa-regular fa-heart");
        });
    });
});