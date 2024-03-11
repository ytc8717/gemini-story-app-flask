document.addEventListener("DOMContentLoaded", function() {
    const storyElement = document.querySelector(".fade-in");
    storyElement.classList.add("show");
});

function validateForm() {
    const imageInput = document.getElementById("image");
    if (!imageInput.files.length) {
        alert("Please select an image.");
        return false;
    }

    // Check the file extension
    const allowedExtensions = ["jpg", "jpeg", "png", "gif"];
    const fileName = imageInput.files[0].name;
    const fileExtension = fileName.split(".").pop().toLowerCase();

    if (!allowedExtensions.includes(fileExtension)) {
        alert("Invalid file type. Please upload an image (JPG, JPEG, or PNG).");
        return false;
    }

    // Show loading spinner
    const spinner = document.querySelector(".spinner");
    spinner.classList.add("loading");
    return true; // Allow the form to submit
}