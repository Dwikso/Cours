#include <stdio.h>

int mutliply(int a) {
  int i = 0;
  for(i = 0; i <= 10; i++) {
    printf("%d x %d = %d\n", a, i, a * i);
  }
  return 0;
}

int main(void) {
  int a;
  printf("Entrez un nombre : ");
  scanf("%d", &a);
  mutliply(a);
  return 0;
}
