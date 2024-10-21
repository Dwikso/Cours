#include <stdio.h>

void hanoi(int nb_diques, int dep, int intermediaire, int dest) {
  if (nb_diques == 1) {
    printf("Depalcer un disque de %d vers %d\n", dep,dest);
  }else {
    hanoi(nb_diques - 1, dep, intermediaire, dest);
    hanoi(1,dep,intermediaire,dest);
    hanoi(nb_diques - 1, intermediaire, dest, dep);
  }
}

int main(void) {
  int nb_diques;
  printf("Entrez le nombre de disques : ");
  scanf("%d", &nb_diques);
  hanoi(nb_diques, 1, 2, 3);
  return 0;
}
