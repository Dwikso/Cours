#include <stdio.h>
#include <string.h>

void inverse(char *str) {
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

int main() {
    char str[] = "Bonjour";
    printf("Avant inversion: %s\n", str);
    inverse(str);
    printf("Après inversion: %s\n", str);
    return 0;
}

