#include <stdio.h>


int dora(int tab[],int t, int taille) {
  int i,j = 0;
  for(i = 0; i < taille; i++) {
    for(j = 0; j < taille; j++) {
      if (tab[i] + tab[j] == t) {
        return 1;
      } 
    }
  }
  return 0;
}


int main(void) {
  int tab[10] = {1,2,3,4,5,6,7,8,9,10};
  int taille = 10;
  int t = 0;
  if (dora(tab, t, taille)) {
    printf("Bien joué\n");
  } else {
    printf("Dommage\n");
  }
}
