#include <stdio.h>

int uniforme(long unsigned int n) {
  int dernier;
  dernier = n % 10;
  n = n/10;
  while (n!=0) {
    if ((n%10) != dernier) return 0;
    n = n/10;
  }
  return 1;
}

int main() {
  int n;
  printf("Entrer un nombre: ");
  scanf("%d", &n);
  if (uniforme(n)) printf("Ce nombre est uniforme.\n");
  else printf("Ce nombre n'est pas uniforme.\n");
  return 0;
}
