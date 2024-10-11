#include <stdio.h>

int main(void) {
  unsigned int entier;
  printf("Entrez un entier :");
  scanf("%d", &entier);
  printf("Les 2 dernires chiffres sont %d \n", entier % 100);
}
