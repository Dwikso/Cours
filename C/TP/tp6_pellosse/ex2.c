#include <stdio.h>
#include <stdlib.h>

int *p;

int allocation(int n) {
  p =(int *) malloc(n * sizeof(int));
  if (p==NULL) {
    return 0;
  } else {
    return 1;
  }
}

int main(void) {
  int n;
  printf("Entrez un nombre : ");
  scanf("%d", &n);
  if (allocation(n)) {
    printf("1\n");
    printf("%p \n", &p[0]);
    free(p);
  } else {
    printf("Cela n'a pas fonctionner 0\n");
  };
  return 0;
}
