// Requirements:
// - give the id "delete-profile-button" to the delete button
// - give the data attribute "data-user-id" to the delete button with the user id as value

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("#delete-profile-button").addEventListener("click", () => {
        const delete_button = document.querySelector("#delete-profile-button");
        if (delete_button) {
            user_id = delete_button.getAttribute("data-user-id");
            fetch(`/profile/delete`)
                .then(function (response) {
                    if (response.status === 200) {
                        window.location.href = `/`;
                    }
                });
        }
        else {
            console.log("Delete button not found");
        }
    });
});