#include <stdio.h>

int main(void) {
  unsigned int a, b, c;
  printf("Entrer un entier : ");
  scanf("%d", &a);
  printf("Entrer un autre entier : ");
  scanf("%d", &b);
  printf("Entrer un troisième entier : ");
  scanf("%d", &c);
  printf("La valeur des entiers sont %d %d %d \n", a, b, c);
  return 0;
}
