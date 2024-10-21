function PGCD(n, m) {
  if (a < b) {
    c = a;
    a = b;
    b = c;
  }
  while (a % b > 0) {
    c = a % b;
    a = b;
    b = c;
  }
  return b;
}
