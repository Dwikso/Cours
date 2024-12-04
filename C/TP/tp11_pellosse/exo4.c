#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

void imprimer_liste_normal(noeud *tete) {
  noeud *courant = tete;
  while (courant != NULL) {
    printf("%d ", courant->element);
    courant = courant->suivant;
  }
  printf("\n");
}

int main(void) {
  noeud *n1 = malloc(sizeof(noeud));
    noeud *n2 = malloc(sizeof(noeud));
    noeud *n3 = malloc(sizeof(noeud));

    n1->element = 10;
    n2->element = 20;
    n3->element = 30;

    n1->suivant = n2;
    n2->suivant = n3;
    n3->suivant = NULL; 

    imprimer_liste_normal(n1);

    free(n1);
    free(n2);
    free(n3);

    return 0;
}
