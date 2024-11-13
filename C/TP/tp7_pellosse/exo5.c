#include <stdio.h>

int inverse_bit(int n, int indice) {
  return (n ^ (1 << indice));
}

int main() {
  int n,i;
  printf("Entrer un nombre entier et un indice: ");
  scanf("%d %d",&n, &i);
  printf("Avant Inversion : %d\n ",n);
  n = inverse_bit(n,i);
  printf("Apres Inversion : %d\n",n);
  return 0;
}
