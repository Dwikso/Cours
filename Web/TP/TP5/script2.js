let variables = "SUSHI"
let pi = Math.PI
let random = Math.floor(Math.random()*100)

function DocWrite() {
    document.open()
    document.write(" <br> Bonjour")
    document.write("<br>")
    document.write("Nombre : ",  42, "<br>")
    document.writeln(variables, "<br>")
    document.writeln(pi, "<br>")
    document.write("Nombre aléatoire : ", random)
    document.close()
}


function temperature(temp) {
    var temp = document.getElementById("temp").value
    if (temp > 38) {
        document.writeln("Il Fait chaud")
    } else {
        document.writeln("Il fait Froid")
    }
}

function getScreenProperties() {
    var screenWidth = window.screen.width
    var screenHeight = window.screen.height
    var screenColorDepth = window.screen.colorDepth
    document.writeln("<br> La taille de l'écran est : ", screenWidth, "x", screenHeight, "<br>")
    document.writeln("La profondeur de couleur est : ", screenColorDepth)
}



getScreenProperties()

DocWrite()
