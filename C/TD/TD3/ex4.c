#include <stdio.h>

int main(void) {
  int i = 0;
  int erreur;

  while (i < 99) {
    printf("Merci d'entrer un nombre qui est soit égal à 99 ou supérieur : ");
    erreur = scanf("%d", &i);

    if (erreur != 1) {
      printf("Erreur: Veuillez entrer un nombre valide.\n");
      getchar();
    }
  }

  printf("%d.\n", i);
  return 0;
}
