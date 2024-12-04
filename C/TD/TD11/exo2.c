#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

int occurence(noeud *tete, int nb) {
  int res = 0;
  while (tete != NULL) {
    if (tete->element == nb) {
      res++;
    }
    tete = tete->suivant;
  }
  return res;
}

int occurence_rec(noeud *tete, int nb) {
    if (tete == NULL) {
        return 0;  
  }
    if (tete->element == nb) {
        return 1 + occurence_rec(tete->suivant, nb);
    } else {
        return occurence_rec(tete->suivant, nb);
    }
}

int main(void) {
  noeud *debut;
  
  noeud A;
  A.element = 1;

  noeud B;
  B.element = 2;

  noeud C;
  C.element = 3;

  noeud D;
  D.element = 1;

  A.suivant = &B;
  B.suivant = &C;
  C.suivant = &D;
  D.suivant = NULL;

  debut = &A;
  printf("occurence(debut, 1) = %d\n", occurence(debut, 1));
  printf("occurence_rec(debut, 1) = %d\n", occurence_rec(debut, 1));
  return 0;
}
