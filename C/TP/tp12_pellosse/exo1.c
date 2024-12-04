#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

void ajouter_element(noeud **tete, int nb) {
  noeud *nouveau = (noeud *)malloc(sizeof(noeud));
  *nouveau = *tete;
  nouveau->element = nb;
  nouveau->suivant = *tete;

  *tete = nouveau;
};
