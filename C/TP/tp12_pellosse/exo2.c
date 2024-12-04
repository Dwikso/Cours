#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

void imprimer_liste(noeud *tete) {
  noeud *courant = tete;
  while (courant != NULL) {
    printf("%d ", courant->element);
    courant = courant->suivant;
  }
  printf("\n");
}

void imprimer_liste_rec(noeud *tete) { 
   noeud *courant = tete; 
    if (courant != NULL) { 
      printf("%d ", courant->element); 
      imprimer_liste_rec(courant->suivant); 
   }  
   printf("\n");
 };

void imprimer_liste_inverse(noeud *tete) {
  noeud *fin = NULL, *courant;
  while(tete != fin) {
    courant = tete;
    while(courant->suivant != fin) {
      printf("%d ", courant->element);
      courant = courant->suivant;
    }
    fin = courant;
  }
}

void imprimer_liste_inverse_rec(noeud *tete) {
  if(tete) {
    imprimer_liste_inverse_rec(tete->element);
    printf("%d ", tete->suivant);
  }
};

void supprimer_premier_element(noeud **tete) {
  if(*tete != NULL) {
    *tete = (*tete)->suivant;
  }
}

void supprimer_maillon(noeud **tete, int nb) {
  if(*tete == NULL) {
    printf("La liste est vide\n");
  }
  else if((*tete)->suivant == nb) {
    (*tete)->suivant = (*tete)->suivant->suivant;
  }
}

void ajouter_element(noeud **tete, int nb) {
  noeud *nouveau = (noeud *)malloc(sizeof(noeud));
  nouveau->element = nb;
  nouveau->suivant = *tete;

  *tete = nouveau;
};

int main (void) {
    noeud *debut;
    debut = NULL;
    ajouter_element(&debut,5);
    ajouter_element(&debut,6);
    ajouter_element(&debut,7);
    ajouter_element(&debut,8);


    supprimer_maillon(&debut,7);
    imprimer_liste(&debut);

    return(0);
}
