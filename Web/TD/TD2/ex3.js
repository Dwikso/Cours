function myPush(tableau, a) {
  tableau[tableau.length] = a;
  return tableau;
}

console.log(myPush([1, 2, 3, 4], 3));
