#include <stdio.h>

int main(void) {

  unsigned short int entier;
  char c;

  scanf("%hu", &entier);
  printf("La lettre est %c", entier);
  scanf("%c", &c);

  printf("Le code ASCII %c est : %d(decimal) et %d(hexadecimal)\n", c, c, c);

  return (0);
}
