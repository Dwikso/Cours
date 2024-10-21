#include <stdio.h>

void init_pointeur_a_NULL(int **p) {
  *p = NULL;
}

int main(void) {
  int i;
  int *q;
  q=&i;
  init_pointeur_a_NULL(&q);
  printf("Apres inititialisation : %p\n", q);
}
