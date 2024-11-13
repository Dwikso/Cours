#include <stdio.h>
#include <stdlib.h>

int somme_recursive_sans_crochets(int *t) {
    if (*t == -1) {
        return 0;
    }
    return *t + somme_recursive_sans_crochets(t + 1);
}

int somme_recursive(unsigned int *t) {
  int somme = 0;
  if (t[0] == -1) {
    return 0;
  } else {
      somme = t[0] + somme_recursive(t + 1);
  }
  return somme;
}

int main() {
    int t[] = {3, 5, 7, 10, -1};  
    int somme = somme_recursive(t);
    printf("La somme des éléments est : %d\n", somme);
    return 0;
}

