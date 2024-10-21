#include <stdio.h>
int main(void) {

  unsigned char i = 'A';
  int j = 1;
  int n = 10;
  int t = 9;
  int a = 34;
  printf("%c %c i=%d %c %c j=%d%c %c", n, t, i, t, a, j, a, n);
  printf("%c %c i=%c %c %c %c", n, t, i, t, a, n);

  return (0);
}
