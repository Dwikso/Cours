function SommeTab(tableau) {
  var i = 0;
  var somme = 0;
  for (i = 0; i < tableau.length; i++) {
    somme += tableau[i];
  }
  return somme;
}

//console.log(SommeTab([1, 2, 3, 4]));

function Maxtab(tableau) {
  var max = tableau[0];
  for (var i = 0; i < tableau.length; i++) {
    if (tableau[i] > max) {
      max = tableau[i];
    }
  }
  return max;
}

// console.log(Maxtab([1, 2, 3, 4]));
