#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generer_nombre(void) {
  return rand() % 60000 + 1;
}

int main(void) {
  int i, nombre_a_deviner;

  srand(time(NULL));
  nombre_a_deviner = generer_nombre();
  
  printf("Le nombre à deviner est %d\n", nombre_a_deviner);
  printf("Entrez un nombre : ");
  scanf("%d", &i);

  while (i != nombre_a_deviner) {
    if (i < nombre_a_deviner) {
      printf("Le nombre est plus grand\n");
    } else {
      printf("Le nombre est plus petit\n");
    }
    printf("Entrez un nombre : ");
    scanf("%d", &i);
  }
  
  printf("Félicitations ! Le nombre était bien %d\n", nombre_a_deviner);

  return 0;
}

