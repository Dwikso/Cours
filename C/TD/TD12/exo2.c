#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

void liberer_toute_liste(noeud *tete) {
  noeud *tmp;
  while (tete != NULL) {
    tmp = tete;
    tete = tete->suivant;
    free(tmp);
  }
}

void liberer_toute_liste_2(noeud *tete) {
  noeud *tmp;
  while (*tete != NULL) {
    tmp = *tete;
    *tete = (*tete)->suivant;
    free(tmp);
  }
  *tete = NULL;
}

int main (void) {
    noeud *n1, n2, n3, n4;
    n1 = (noeud *) malloc(sizeof(noeud));
    (*n1).element = 2;
    n2.element = 6;
    n3.element = 8;
    n4.element = 6;
    (*n1).suivant = &n2;
    n2.suivant = &n3;
    n3.suivant = &n4;
    n4.suivant = NULL;
    printf("%d \n",existe_rec(n1,3));
    return(0);
}


