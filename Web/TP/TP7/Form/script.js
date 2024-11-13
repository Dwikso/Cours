document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("form").addEventListener("submit", function(event) {
        event.preventDefault();


        const username = document.getElementById("name").value;
        const email = document.getElementById("email").value;


        if (!isValidUsername(username)) {
            console.log("Erreur : le pseudo doit contenir entre 8 et 25 caractères alphanumériques.");
            document.getElementById("name").style.color = 'red';
            return;
        }

        if (isValidUsername(username)) {
            alert("Compte enregistrer")
        }

        console.log("Nom:", username);
        console.log("Email:", email);
    });


function isValidUsername(username) {

    if (username.length < 8 ||3 username.length > 25) {
        return false;
    }

    for (let i = 0; i < username.length; i++) {
        const char = username[i];
        if (!(char >= 'a' && char <= 'z') && !(char >= 'A' && char <= 'Z') && !(char >= '0' && char <= '9')) {
            return false;
        }
    }

    return true;
}

function isValidEmail(email) {
    if (email.length > 25) {
        return false;
    }
}



});
