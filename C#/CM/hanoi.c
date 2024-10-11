#include <stdio.h>

int hanoi(int n, int dep, int intermediare,  int dest) {
  if(n == 1) {
    printf("Deplacer un disque de %d vers %d\n", dep, dest)
  } else {
    hanoi(n-1, dep, dest, intermediare);
    hanoi(1, intermediare, dep, dest);
  }
}

