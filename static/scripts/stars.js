const starFull = "&#9733";
const starOutline = "&#9734";

function convertRatingToStars(rating) {
    const ratingValue = Math.floor(+rating.innerHTML) / 2;
    rating.innerHTML = "";
    for (let i = 0; i < 5; i++) {
        rating.innerHTML += i <= ratingValue ? starFull : starOutline;
    }
}