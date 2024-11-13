#include <stdio.h>
#include <stdlib.h>

int nbr_occurences(int tab[], int nbre) {
  if (*tab == -1) {
    return 0;
  }
  if (*tab == nbre) {
    return 1 + nbr_occurences(tab + 1, nbre);
  }
  return nbr_occurences(tab + 1, nbre);
}

int main(void) {
  int tab[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, -1};
  int nbre = 1;
  printf("%d\n", nbr_occurences(tab, nbre));
  return 0;
}
