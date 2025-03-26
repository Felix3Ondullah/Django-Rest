document.addEventListener("DOMContentLoaded", function () {
    console.log("Django-Rest Admin Loaded Successfully!");

    // Example: Change the page title dynamically
    document.title = "Django-Rest | Admin Panel";

    // Example: Change the background color of the navbar on load
    let navbar = document.querySelector('.navbar');
    if (navbar) {
        navbar.style.backgroundColor = "#16213e";
    }
});
