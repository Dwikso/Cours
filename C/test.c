#include <stdio.h>

int trouver_paire(int n, int *a, int *b) {
  int current, precendent;
  
  printf("Entrez un entier : ");
  scanf("%d", &precendent);

  for(int i = 0; i < n; i++) {
    printf("Entrez un entier : ");
    scanf("%d", &current);
    if(current + precendent == 0) {
      *a = précendent;
      *b = current;
      return 1;
    }
    precendent = current;
  }
  return 0;
}
