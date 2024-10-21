#include <stdio.h>
#include <stdbool.h>

bool tab_trie(int tab[],int taille) {
  int i;
  for(i = 0; i < taille; i++) {
    if (tab[i] < tab[i +1]) {
      return false;
    }
  }
  return true;
}

int main() {
  int tab[] = {5,4,3,2,1};
  int taille = 5;
  if (tab_trie(tab,taille)) {
    printf("tab est un trié de maniere décroissante\n");
  } else {
    printf("tab n'est pas un trié de maniere décroissante\n");
  }
  return 0;
}
