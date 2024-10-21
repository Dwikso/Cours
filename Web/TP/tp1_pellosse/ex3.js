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
//

function nbIterHamAlt(n) {
  var i = 1;
  var somme = 0;
  while (n > -Math.log(2) - somme) {
    if (i % 2 === 0) {
      somme += 1 / i;
    } else {
      somme -= 1 / i;
    }
    i++;
    console.log(somme, i);
  }
  return i;
}

console.log(nbIterHamAlt(1));
