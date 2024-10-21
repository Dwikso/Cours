#include <stdio.h>

int Hofstaders(int n) {
  if (n < 3) return(0);
  else {
    return Hofstaders((n - Hofstaders(n-1))) + Hofstaders((n - Hofstaders(n-2)));
  }
}

int main(void) {
  int n;
  printf("Entrez un nombre : ");
  scanf("%d", &n);
  printf("Résultat : %i \n ", Hofstaders(n));
  return(0);
}
