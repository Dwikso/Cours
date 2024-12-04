#include <stdio.h>
#include <stdlib.h>

#define Taille 2000

void liberer(int **p) {
    free(*p);
    *p = NULL;
}

int main(void) {
    int *p = (int *)malloc(Taille * sizeof(int)); 
    if (p == NULL) { 
        printf("Échec de l'allocation mémoire.\n");
        return 1;
    }
    
    liberer(&p); 
    printf("La nouvelle valeur du pointeur est : %p\n", (void *)p);
    return 0;
}

