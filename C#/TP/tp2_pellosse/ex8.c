#include <stdio.h>

int main(void) {
  printf("Char : %ld \n", sizeof(char));
  printf("Int :  %ld \n", sizeof(int));
  printf("Int :  %ld \n", sizeof(short));
  printf("Long :  %ld \n", sizeof(long));
  printf("Double :  %ld \n", sizeof(double));
  printf("Signed Short :  %ld \n", sizeof(signed short));
  printf("Float :  %ld \n", sizeof(float));
  return 0;
}
