#include <stdio.h>
#include <stdlib.h>

struct _liste {
  int nombre;
  struct _liste *suivant;
};

typedef struct _liste liste;

void imprimer_liste_normale(liste *tete) {
    liste *current = tete;
    while (current != NULL) {
        printf("%d ", current->nombre); 
        current = current->suivant; 
  }
    printf("\n"); 
}

int main() {
    
}

