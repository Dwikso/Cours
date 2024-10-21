#include <stdio.h>

int bit_a_bit(int nb) {
  if (nb == 0) return 0;
  else return (nb & (nb-1)) == 0;
}

int main() {
  int nb;
  printf("Entrez un nombre: ");
  scanf("%d", &nb);
  int res = bit_a_bit(nb);
  if (res) {
    printf("Le nombre %d est pas une puissance de 2. \n", nb);
  } else {
    printf("Le nombre %d n'est pas une puissance de 2. \n", nb);
  }
}
