#include <stdio.h>

int main(void) {
  int i;
  i = 0;
  while (getchar() != '\n') {
    i++;
  }
  printf("%d \n", i);
  return 0;
}
