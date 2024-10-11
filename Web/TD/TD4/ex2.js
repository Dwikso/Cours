function distEuclide(a, b) {
  p = b.p - a.p;
  q = b.q - a.q;
  return Math.sqrt(Math.pow(p, 2) + Math.pow(q, 2));
}

const x = { p: 1, q: 2 };
const y = { p: 4, q: 6 };

console.log("Exercice 2 : Distance Euclide:", distEuclide(x, y));
