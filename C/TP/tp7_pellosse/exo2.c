#include <stdio.h>

int diviseurs_stricts(int n) {
  int c = 0;
  int i;
  for (i=1; i<n; i++) {
    if (n%i == 0)
    c++;
  }
  return c;
}

int main() {
  int n;
  printf("Entrer un nombre: ");
  scanf("%d", &n);
  printf("%d\n",diviseurs_stricts(n));
  return 0;
}
