#include <stdio.h>
#include <stdlib.h>

#define Taille 2000

void liberer(int **p) {
  *p = NULL;
}

int main(void) {
  void liberer();
  int *p=(int *) malloc(Taille*sizeof(int));
  liberer();
  printf("La nouvelle du pointeur est : %p \n", p);
  return 0;
}
