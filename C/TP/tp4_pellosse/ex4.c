#include <stdio.h>


int main(void)
{
    int result = 0;
    char bit;
    printf("Entrez une sequence de bits : \n");
    while ((bit = getchar()) != '\n'){
      if (bit == '0' || bit == '1'){
        result = (result << 1) | (bit - '0');
      }else{
        printf("Erreur : Veuillez entrer uniquement des bits .\n");
        return 1;
      }
    }

    printf("La valeur entière est : %d\n", result);
    return 0;
}
