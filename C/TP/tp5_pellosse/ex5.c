#include <stdio.h>

int cmpt_nb_in_nb(unsigned int nb, unsigned int c) {
  int cpt = 0;
  for(int i = 0; i <= nb; i ++) {
    int nombre = i;
    while (nombre > 0) {
      if (nombre % 10 == c) {
        cpt++;
      }
      nombre /=10;
    }

    if (i==0 && c ==0) {
      cpt++;
    }
  }
  return cpt;
}

int main() {
  int c = 7;
  int n = 100;

  int result = cmpt_nb_in_nb(n, c);
  printf("Le nombre de chiffres %d est présent %d dans le nombre %d\n", c, result, n);
}
