#include <stdio.h>

int disjoint(int tabA[], int tabB[], int tailleTab) {
  int i,j;
  for(i=0; i < tailleTab; i++) {
    for(j=0;j < tailleTab;j++) {
      if (tabA[i] == tabB[j]) {
        return 0;
      }
    }
  }
  return 1;
}

int main() {
  int tabA[5] = {1,2,3,4,5};
  int tabB[5] = {6,7,8,9,10};
  int tailleTab = 5;
  if (disjoint(tabA,tabB,tailleTab)) {
    printf("Les deux tableaux sont disjoints\n");
  } else {
    printf("Les deux tableaux ne sont pas disjoints\n");
  }
  return 0;
}



