#include <stdio.h>

int main(void) {
  unsigned int a = 1, b = 2;
  a = a + b;
  b = a - b;
  a = a - b;
  b = b;
  printf("En echangelent les valeurs a= %d et b = %d \n", a, b);
  return 0;
}
