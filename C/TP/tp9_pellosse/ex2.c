#include <stdio.h> 
#include <stdlib.h>

int mystere2(unsigned int a, unsigned int b) {
  unsigned char a_ce_stade = 0;
  if (! (a^b)) return 0;
  while (a && b) {
    if ((a&1) && (!(b&1))) a_ce_stade = 1;
    else if ((!(a&1)) && (b&1)) a_ce_stade = -1;
    a >>= 1;
    b >>= 1;
  }
  if (a) return 1;
    else if (b) return -1;
      else return a_ce_stade;
  }


int main(void) {
  unsigned int a = 3;
  unsigned int b = 3;
  printf("%d\n", mystere2(a, b));
  return 0;
}
