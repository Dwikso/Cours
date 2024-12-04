#include <stdio.h>
#include <stdlib.h>

struct _noeud {
  int element;
  struct _noeud *suivant;
};

typedef struct _noeud noeud;

noeud *creation_de_liste(void) {
    noeud *tete = NULL;
    int valeur;

    printf("Entrez des entiers (nombre négatif pour arrêter) :\n");
    scanf("%d", &valeur);

    while (valeur >= 0) {
        noeud *nouveau = malloc(sizeof(noeud));
        nouveau->element = valeur;
        nouveau->suivant = tete; 
        tete = nouveau;

        scanf("%d", &valeur); 
    }

    return tete; 
}

noeud creation_de_liste_v2(noeud **tete) {
  noeud *tete = NULL;
    int valeur;

    printf("Entrez des entiers (nombre négatif pour arrêter) :\n");
    scanf("%d", &valeur);

    while (valeur >= 0) {
        noeud *nouveau = malloc(sizeof(noeud));
        nouveau->element = valeur;
        nouveau->suivant = tete; 
        tete = nouveau;

        scanf("%d", &valeur); 
    }

    return tete; 
}

int main(void) {}
