#include <stdio.h>
#include <stdlib.h>

#define taille 10

int inverse(int tab[]) {
  int i = 0;
  while (tab[i] != -1) {
    i++;
  }
  for (int j = i - 1; j >= 0; j--) {
    printf("%d \n", tab[j]);
  }
  return 0;
}


int main(void) {
  int t[taille] = {1, 2, 3, 4, 5, 6, 7, 8, 9, -1};
  inverse(t);
  return 0;
}
