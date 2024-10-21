function myShift(tableau) {
  var elt = tableau[0];
  var i = 0;
  for (i; i < tableau.length - 1; i++) {
    tableau[i] = tableau[i + 1];
  }
  return elt;
}

console.log(myShift([1, 2, 3], 1));
