#include <stdio.h>
#include <stdlib.h>

#define k 5

int tous_different(unsigned int *t) {
  int i,j;
  for(i = 0; i < k; i++) {
    for(j = i + 1; j < k; j++) {
      if (t[i] == t[j]) {
        return 0;
      }
    }
  }
  return 1;
}

int main(void) {
    unsigned int t[] = {1, 2, 3, 4, 5};  // Corrected to an array
    if (tous_different(t)) {
        printf("Les éléments sont différents\n");
    } else {
        printf("Tous les éléments ne sont pas différents\n");
    }
}
