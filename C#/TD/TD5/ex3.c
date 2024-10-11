#include <stdio.h>

int main(void) {
  int cmpt = 0;
  int nb;
  printf("Entrer un nombre entier: ");
  scanf("%d", &nb);
  for(int i = 1; i < nb; i++ ) {
    if( i % 2 == 0 ) {
      cmpt += 1;
    }
  }
  printf("nb = %d, cmpt = %d\n", nb, cmpt);
  return 0;
}
