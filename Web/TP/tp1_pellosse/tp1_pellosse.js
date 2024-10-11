// Exo1

function maxi(n, m) {
  if (n > m) {
    return n;
  } else {
    return m;
  }
}

// Exo2

// console.log(maxi(2, 3));

function abs(x) {
  if (x < 0) {
    return -x;
  } else if (x === 0) {
    return x;
  } else {
    return x;
  }
}

// console.log(0);

// Exo3

function harm(n) {
  var i = 1;
  var somme = 0;
  if (n === 0 || n === 1) {
    return n;
  } else {
    while (i <= n) {
      somme += 1 / i;
      i++;
    }
    return somme;
  }
}

//console.log(harm(0));
//console.log(harm(1));
//console.log(harm(100));
//console.log(harm(1000));

function harmAlt(n) {
  var somme = 0;
  if (n === 0 || n === -1) {
    return n;
  } else {
    while (n !== 0) {
      if (n % 2 === 0) {
        somme += 1 / n;
        n -= 1;
      } else {
        somme -= 1 / n;
        n -= 1;
      }
    }
    return somme;
  }
}

// console.log(harmAlt(0));
// console.log(harmAlt(1));
// console.log(harmAlt(1000));
// console.log(harmAlt(100000));

function nbIterHamAlt(n) {
  var i = 0;
  var somme = 0;
  while (n < abs(-Math.log(2) - somme)) {
    i++;
    if (i % 2 === 0) {
      somme += 1 / i;
    } else {
      somme -= 1 / i;
    }
  }
  return i;
}

console.log(nbIterHamAlt(1));
console.log(nbIterHamAlt(0.1));
console.log(nbIterHamAlt(0.001));
console.log(nbIterHamAlt(0.00001));

// Exo4
function celsiusToFahrenheit(n, m) {
  var i = 0;
  for (i = 0; i <= n; i += m) {
    console.log((9.0 * i) / 5.0 + 32.0);
  }
}

// celsiusToFahrenheit(10, 2);

// Exo5
//
function abregebinaire(n, m) {
  if (m === "K") {
    return n * 1024;
  } else if (m === "M") {
    return n * 1024 ** 3;
  } else if (m === "G") {
    return n * 1024 ** 6;
  } else if (m === "T") {
    return n * 1024 ** 9;
  } else {
    return false;
  }
}

/* console.log(abregebinaire(2, "K")); */
