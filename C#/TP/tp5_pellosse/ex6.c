#include <stdio.h>

int code_substitution(char letter, int c) {
    if (letter >= 'A' && letter <= 'Z') {
        return (letter - 'A' + c) % 26 + 'A';      }
    return letter;  
}

int main() {
    int c;
    char letter;

    printf("Entrez la clé de décalage : ");
    scanf("%d", &c);

    printf("Entrez le caractère à remplacer : ");
    scanf(" %c", &letter);  

    printf("La lettre chiffrée avec k = %d donne : %c\n", c, code_substitution(letter, c));

    return 0;
}

