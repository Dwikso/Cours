#include <stdio.h>

int main(void) {
  unsigned int a;
  scanf("%u", &a);
  a = a >> 2;
  a = a & 1;
  printf("%u \n", a);
  return 0;
}
