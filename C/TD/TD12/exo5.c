#include <stdio.h>
#include <stdlib.h>


struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef strcut _noeud noeud;

void rajouter_element_fin_rec(noeud **tete, int nb) {
  if(*tete != NULL) rajouter_element_fin_rec(&(*tete) ->suivant,nb);
  else rajouter_element_fin_debut(tete, nb)
}
