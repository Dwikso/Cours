#include <stdio.h>

int main(void) {
  int t[3] = {10,-20,320};
  printf("La taille de &t est : %lu \n", sizeof(&t));
  printf("La taille de t[0] est : %lu \n", sizeof(t[0]));
  printf("La taille de &t[0] est : %lu \n", sizeof(&t[0]));
  printf("La taille de t est : %lu \n", sizeof(t));
  return 0;
}
