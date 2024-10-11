function supprimer(chaine, pattern) {
  var i = 0;
  var newChaine = "";
  var mot = chaine.split(" ");
  for (i; i < mot.length; i++) {
    if (mot[i] !== pattern) {
      if (newChaine !== "") {
        newChaine += " ";
      }
      newChaine += mot[i];
    }
  }
  return newChaine;
}

console.log(supprimer("Bonjour tout le monde", "tout"));

function replace(chaine, pattern, newpattern) {
  var i = 0;
  var newChaine = "";
  var mot = chaine.split(" ");
  for (i; i < mot.length; i++) {
    if (mot[i] === pattern) {
      newChaine += newpattern;
    } else {
      newChaine += mot[i];
    }
    if (i < mot.length - 1) {
      newChaine += " ";
    }
  }
  return newChaine;
}

console.log(replace("Bonjour tout le monde", "Bonjour", "test"));
