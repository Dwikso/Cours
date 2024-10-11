#include <stdio.h>

int main(void) {
  int *p;
  double *p1;
  printf("La mémoire de p est : %ld \n", sizeof(p));
  printf("La mémoire de p1 est : %ld \n", sizeof(p1));
}

// la mémoire de p et de p1 est la même
