//Entier miroir

#include <stdio.h>

int entierMiroir(int nombre) {
  int miroir = 0;
  while (nombre > 0) {
    miroir = miroir * 10 + nombre % 10;
    nombre = nombre / 10;
  }
  return miroir;
}


int main() {
  int nombre, miroir;
  printf("Entrez un nombre: ");
  scanf("%d", &nombre);
  miroir = entierMiroir(nombre);
  printf("Le miroir de %d est %d\n", nombre, miroir);
  return 0;
}
