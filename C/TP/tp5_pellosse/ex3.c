#include <stdio.h>

int est_puissance_de_2(unsigned int n)
{
    if (n == 0)
        return 0;
    while (n != 1){
      if (n % 2 != 0)
        return 0;
        n = n / 2;
    }
    return 1;
}

int main()
{
    unsigned int nb;
    printf("Entrez un nombre entier positif: ");
    scanf("%u", &nb);
    printf("Vous avez entré: %u\n", nb);
    int res = est_puissance_de_2(nb);
    if (res)
    {
        printf("%u est une puissance de 2.\n", nb);
    }
    else
    {
        printf("%u n'est pas une puissance de 2.\n", nb);
    }
    return 0;
}
