// Exercice 2

caracteresSpeciaux = [
  "!",
  '"',
  "#",
  "$",
  "%",
  "&",
  "'",
  "(",
  ")",
  "*",
  "+",
  ",",
  "-",
  ".",
  "/",
  ":",
  ";",
  "<",
  "=",
  ">",
  "?",
  "@",
  "[",
  "\\",
  "]",
  "^",
  "_",
  "`",
  "{",
  "|",
  "}",
  "~",
  "§",
  "±",
  "£",
  "¤",
  "¥",
  "©",
  "«",
  "®",
  "°",
  "µ",
  "»",
  "¿",
  "×",
  "÷",
  "ƒ",
  "ø",
  "π",
  "Ω",
];

function estPalindrome(str) {
  var i = 0;
  var j = str.length - 1;
  for (i; i < str.length; i++) {
    for (j; j >= 0; j--) {
      if (str[i] === str[j]) {
        return true;
      } else {
        return false;
      }
    }
  }
}

console.log(estPalindrome("toto"));
console.log(estPalindrome("SOS"));

function estPalindrome2(str) {
  var i = 0;
  var newChaine = "";
  for (i; i < str.length; i++) {
    if (str[i] !== " " && caracteresSpeciaux.indexOf(str[i]) === -1) {
      newChaine += str[i].toLowerCase();
    }
  }
  console.log(newChaine);
  return estPalindrome(newChaine);
}

console.log(estPalindrome2("esope reste elu par cette crapule et se repose"));
console.log(estPalindrome2("Eh ca va la vache ?"));
console.log(estPalindrome2("La mariée ira mal."));

// Exercice 2

function CompteMots(phrase) {
  let mots = phrase.split(" ");
  return mots.length;
}
console.log(CompteMots("la maman de Colette et de Daniel"));

function CompteMots2(phrase) {
  let mots = phrase.split(" ");
  return mots.filter((mot) => mot.length > 0).length;
}

console.log(CompteMots2(" la maman    de Colette et de   Daniel  "));

// Exercice 3

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
