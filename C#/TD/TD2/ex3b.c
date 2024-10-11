#include <stdio.h>

int main(void) {
  unsigned int a, b, c;
  scanf("%u %u", &a, &b);
  c = a;
  a = b;
  b = c;
  printf("a=%u, b=%u \n", a, b);
  return 0;
}
