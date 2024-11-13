#include <stdio.h>


int puissance_2(int a) {
  if !(a) return 0;
  while(!(a&1)) a >>= 1;
  a >> = 1
  return (!(a));
}


int main(void) {
  int a = 16;
  printf("%d \n", puissance_2(a));
  return 0;
}
