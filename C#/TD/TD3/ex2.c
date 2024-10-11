#include <stdio.h>

int main(void) {
  char chaine;
  int i;
  i = 0;
  chaine = getchar();
  while (chaine != '\n') {
    chaine = getchar();
    i++;
  }
  printf("%d", i);
  return 0;
}
