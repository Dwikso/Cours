#include <stdio.h>

int echange(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
  return 0;
}

int main() {
  int a = 5, b = 10;
  printf("a = %d, b = %d\n", a, b);
  echange(&a, &b);
  printf("a = %d, b = %d\n", a, b);
  return 0;
}
