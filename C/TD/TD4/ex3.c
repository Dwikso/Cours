#include <stdio.h>

char last_bit(int n) {
  return (n&1);
}

int del_bit(int n) {
  return n >> 1;
}

int main(void) {
  char b;
  b = 1
  while(b <= 0) {
    printf("%d", last_bit(b));
    a = del_bit(b);
    b = b+1;
  }
}
