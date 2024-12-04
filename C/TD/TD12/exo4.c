#include <stdio.h>
#include <stdlib.h>


struct _noeud {
  int element;
  struct _noeud *suivant;
  struct _noeud *precedent;
};

typedef strcut _noeud noeud;

void rajouter_element_debut(noeud **tete, int nb) {
  noeud *n = (noeud *)malloc(sizeof(noeud));
  *n = *tete;
  n->element = nb;
  n->suivant = *tete;
  n->precedent = NULL;

  if (*tete != NULL) {
    (*tete)->precedent = n;
  }
  *tete = n;
}

void rajouter_element_fin_rec(noeud **tete, int nb) {
  if(*tete != NULL) rajouter_element_fin_rec(&(*tete) ->suivant,nb);
  else rajouter_element_fin_debut(tete, nb)
}
