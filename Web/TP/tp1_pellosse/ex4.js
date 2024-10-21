function celsiusToFahrenheit(n, m) {
  var i = 0;
  for (i = 0; i <= n; i += m) {
    console.log((9.0 * i) / 5.0 + 32.0);
  }
}

celsiusToFahrenheit(10, 2);
