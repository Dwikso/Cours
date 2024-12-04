#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud noeud;
};

typedef struct _noeud noeud;


void rajouter_element_debut(noeud **tete, int nb) {
  noeud *n = (noeud *)malloc(sizeof(noeud));
  *n = *tete;
  n->element = nb;
  n->suivant = *tete;

  *tete = n;
};
