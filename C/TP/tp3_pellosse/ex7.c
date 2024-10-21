#include <stdio.h>

int main(void) {
  int allumettes, joueur;
  printf("Entrez un nombre d'allumetes : ");
  scanf("%d", &allumettes);
  while (allumettes != 0) {
    printf("joueur 1 : retirer 1, 2 ou 3 allumettes  :");
    scanf("%u", &joueur);
    allumettes -= joueur;
    if (allumettes <= 0) {
      printf("joueur 1 a perdu");
      break;
    } else {
      printf("Il reste %u allumettes \n", allumettes);
    }
    printf("joueur 2 : retirer 1, 2 ou 3 allumettes  :");
    scanf("%u", &joueur);
    allumettes -= joueur;
    if (allumettes <= 0) {
      printf("joueur 2 a perdu \n");
      break;
    } else {
      printf("Il reste %u allumettes \n", allumettes);
    }
  }
}
