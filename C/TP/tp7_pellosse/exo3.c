#include <stdio.h>

#define K 5 

void fusion(int t1[], int t2[], int resultat[], int taille) {
    int i = 0, j = 0, k = 0;

    while (i < taille && j < taille) {
        if (t1[i] < t2[j]) {
            resultat[k++] = t1[i++];
        } else {
            resultat[k++] = t2[j++];
        }
    }

    while (i < taille) {
        resultat[k++] = t1[i++];
    }

    while (j < taille) {
        resultat[k++] = t2[j++];
    }
}

int main() {
    int t1[K] = {1, 3, 5, 7, 9}; 
    int t2[K] = {2, 4, 6, 8, 10}; 
    int resultat[2 * K]; 

    fusion(t1, t2, resultat, K);

    printf("Tableau fusionné : ");
    for (int i = 0; i < 2 * K; i++) {
        printf("%d ", resultat[i]);
    }
    printf("\n");

    return 0;
}

