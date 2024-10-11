#include <stdio.h>

int main(void) {
  int n;
  int res;
  do {
    printf("\nMerci d'introduire un nombre positif ou nul : ");
    res = scanf("%d", &n);
    while(getchar() != '\n');
  } while((res != 1) || (n < 0));
    printf("\nLe nombre lu est : %d\n", n);
  return 0;
}
