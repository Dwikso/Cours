#include <stdio.h>
#include <stdlib.h>

int isUpper(char c) {
    return (c >= 'A' && c <= 'Z');
}

int isLower(char c) {
    return (c >= 'a' && c <= 'z');
}

char processMot(int n) {
    char *mot = (char *)malloc((n + 1) * sizeof(char));
    if (mot == NULL) {
        printf("Erreur d'allocation mémoire");
        return(1);
    }
    printf("Entrez le mot : ");
    for (int i = 0; i < n; i++) {
        mot[i] = getchar();
    }
    int lowerCpt = 0;
    int upperCpt = 0;
    char *lowerLettres = (char *)malloc((n + 1) * sizeof(char));
    char *upperLettres = (char *)malloc((n + 1) * sizeof(char));
    if (lowerLettres == NULL || upperLettres == NULL) {
        printf("Erreur d'allocation mémoire");
        free(mot);
        return(1);
    }
    for (int i = 0; i < n; i++) {
        if (isLower(mot[i])) {
            lowerLettres[lowerCpt++] = mot[i];
        } else if (isUpper(mot[i])) {
            upperLettres[upperCpt++] = mot[i];
        }
    }
    printf("Lettres minuscules (%d) : %s\n", lowerCpt, lowerLettres);
    printf("Lettres majuscules (%d) : %s\n", upperCpt, upperLettres);
    free(mot);
    free(lowerLettres);
    free(upperLettres);
}

int main(void) {
    int n;
    printf("Entrez un nombre : ");
    scanf("%d", &n);
    processMot(n);
    return 0;
}
