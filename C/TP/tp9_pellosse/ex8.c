#include <stdio.h>

int nbr_occurences(int tab[], int nbre) {
  if (*tab == -1) {
    return 0;
  }
  if (*tab == nbre) {
    return 1 + nbr_occurences(tab + 1, nbre);
  }
  return nbr_occurences(tab + 1, nbre);
}


int nb_1(int a) {
  if (a == 0) {
    return 0;
  }

}
