#include <stdio.h>
#include <string.h>
#include <stdbool.h>


#define N 8

void initialiser_echiquer(char echiquer[N][N]) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      echiquer[i][j] = ' ';
    }
  }
}

void imprimer_echiquer(char echiquer[N][N]) {
  int i,j;
  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      printf("%c", echiquer[i][j]);
    }
    printf("\n");
  }
}

int est_entre_0_e_7(int c) {
  return (c >= '0' && c <= '7') ? (c - '0') : -1;
}

int est_piece_echiquier(int c) {
  switch (c) {
    case 't':
    case 'f':
    case 'k':
    case 'p':
    case 'q':
    case 'c':
    case 'T':
    case 'F':
    case 'K':
    case 'P':
    case 'Q':
    case 'C':
      return 1;
    default:
      return 0;
  }
}


bool lire_echiquier(char echiquer[N][N]) {
  int i,j;
  while(getchar() != '$') {

  }
}


int main() {
    char tests[] = {'A', 'B', 'f', 't', 'k', 'C'};
    int nb_tests = 6;

    for (int i = 0; i < nb_tests; i++) {
        char c = tests[i];
        printf("est_entre_0_et_7('%c') = %d\n", c, est_piece_echiquier(c));
    }

    return 0;
}
