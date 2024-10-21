#include <stdio.h>

int mystere(int n) {
  int i, s = 0;
  for (i=1; i<=n; i++) {
    s = s + i/n;
  }
  return s;
}

int main(void) {
  int n;
  printf("Entrez un nombre : ");
  scanf("%d", &n);
  printf("Résultats : %i \n", mystere(n));
}
