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

int existe(noeud *tete, int nb) {
  noeud *courant = tete;
  while(courant != NULL) {
    if (courant->element == nb) {
      return 1;
    }
    courant = courant->suivant;
  }
  return 0;
}

noeud *existe_v2(noeud *tete, int nb) {
  noeud *courant = tete;
  while(courant != NULL) {
    if (courant->element == nb) {
      return courant;
    }
    courant = courant->suivant;
  }
  return NULL;
}

noeud *creation_de_liste(void) {
    noeud *tete = NULL;
    int valeur;

    printf("Entrez des entiers (nombre négatif pour arrêter) :\n");
    scanf("%d", &valeur);

    while (valeur >= 0) {
        noeud *nouveau = malloc(sizeof(noeud));
        if (!nouveau) { 
            printf("Erreur : Allocation mémoire échouée.\n");
            while (tete != NULL) {
                noeud *temp = tete;
                tete = tete->suivant;
                free(temp);
            }
            return NULL;
        }

        nouveau->element = valeur;
        nouveau->suivant = tete; 
        tete = nouveau;

        scanf("%d", &valeur); 
    }

    return tete; 
}

int main(void) {
    noeud *liste = creation_de_liste();
    int nb = 5;

    if (liste == NULL) {
        printf("Aucune liste n'a pu être créée en raison d'une erreur.\n");
    } else {
        printf("Liste chaînée créée :\n");
        imprimer_liste_normal(liste); // Afficher la liste
      
        noeud *result = existe_v2(liste,nb);
        if (result != NULL) {
            printf("L'élément %d existe dans la liste.\n", nb);
        } else {
            printf("L'élément %d n'existe pas dans la liste.\n", nb);
        }
    }

    while (liste != NULL) {
        noeud *temp = liste;
        liste = liste->suivant;
        free(temp);
    }

    return 0;
}
