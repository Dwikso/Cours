#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

int existe_rec(noeud *tete, int nb) {
  if(tete == NULL) return 0;
  else {
    if (tete->element == nb) {
      return 1;
    } else {
      return existe_rec(tete->suivant, nb);
    }
  }
}

int main (void) {
    noeud *n1, n2, n3, n4;
    n1 = (noeud *) malloc(sizeof(noeud));
    (*n1).element = 2;
    n2.element = 6;
    n3.element = 8;
    n4.element = 3;
    (*n1).suivant = &n2;
    n2.suivant = &n3;
    n3.suivant = &n4;
    n4.suivant = NULL;
    printf("%d \n",existe_rec(n1,3));
    return(0);
}
