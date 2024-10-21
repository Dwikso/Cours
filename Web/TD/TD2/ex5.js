function ChainedeCarac(str) {
  var mot = str.split(" ");
  var longeur = 0;
  var i = 0;
  for (i; i < mot.length; i++) {
    if (mot[i].length > longeur) {
      longeur = mot[i].length;
    }
  }
  return longeur;
}

console.log(ChainedeCarac("Bonjour tout le monde"));
