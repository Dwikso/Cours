#include <stdio.h>

int main(void) {

  unsigned char x;
  unsigned char distance;

  scanf("%c", &x);
  distance = x - 'a';
  printf("%c \n", distance + 'A');
  return (0);
}
