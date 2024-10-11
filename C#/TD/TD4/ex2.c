#include <stdio.h>

int main(void) {
  unsigned int n , res = 0;
  scanf("%x", &n);
  while (n != 0) {
    res += n % 10;
    n /= 10;
  }
  printf("%d\n", res);
}
