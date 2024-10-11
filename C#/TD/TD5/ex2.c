#include <stdio.h>

int bit_a_bit(int nb) {
    if (nb == 0) return 0; 
    return (nb % 2) + bit_a_bit(nb / 2);
}

int main() {
  int nb;
  printf("Entrez un nombre: ");
  scanf("%d", &nb);
  printf("Le nombre %d a %d bits.\n", nb, bit_a_bit(nb));
}
