#include <stdio.h>

int main(void) {
  unsigned char i;
  unsigned short int j=256;
  for (i=0; i!=j; i++) {
    printf("Le caractère numéro %d est : %c \n", i, i);
  }
  return 0;
}
