function distGen(a, b, f) {
  return f(a, b);
}

function distEuclideGen(a, b) {
  var sum = 0;
  for (var property in a) {
    sum += (a[property] - b[property]) ** 2;
  }
}
