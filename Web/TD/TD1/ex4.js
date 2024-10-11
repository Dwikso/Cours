function estPremier(n) {
  var estPremier = true;
  if (n < 2 || (n > 2 && n % 2 == 0)) {
    return false;
  }
  var i = 3;
  while (estPremier && i <= Math.sqrt(n)) {
    if (n % i == 0) {
      estPremier = false;
    }
    i += 2;
  }
  return estPremier;
}

console.log(estPremier(10));
