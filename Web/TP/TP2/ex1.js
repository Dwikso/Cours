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

// console.log(estPalindrome("toto"));
// console.log(estPalindrome("SOS"));

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
