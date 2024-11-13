#include <stdio.h>

int main(void) {
  int t[3] = {10,-20,320};
  printf("l'adresse de t est : %p \n", &t);
  printf("l'adresse de t[0] est : %p \n", &t[0]);
  printf("la valeur de t est : %p \n", t);
  return 0;
}
