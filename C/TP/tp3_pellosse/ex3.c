#include <stdio.h>

int main(void) {
  int somme = 0;
  int nombre;

  printf("Entrez un nombre : ");
  scanf("%d", &nombre);

  for (int i = 1; i < nombre; i++) {
    if (nombre % i == 0) {
      somme += i;
      if (somme == nombre) {
        printf("Le nombre est parfaits : %d \n", i);
      } else {
        printf("Le nombre n'est pas parfaits : %d \n", i);
      }
    }
  }
  return 0;
}
