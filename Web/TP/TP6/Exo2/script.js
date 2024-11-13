document.getElementById("stylesform").addEventListener("submit", function (event) {
    event.preventDefault();
    const selectedValue = document.getElementById("styleSelect").value;

    const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
    stylesheets.forEach(stylesheet => {
        stylesheet.media = "none";
    });

    const selectedStylesheet = document.getElementById(selectedValue);
    if (selectedStylesheet) {
        selectedStylesheet.media = "all";
    }
});
