#include <stdio.h>
#include <stdlib.h>


int allocation(int n) {
  int *tab = (int *)malloc(n * sizeof(int));
    if (tab == NULL)
    {
        printf("Échec de l'allocation mémoire.\n");
        return 1;
    }

    printf("Vous avez entré la taille : %u\n", n);

    printf("Entrez %u entiers :\n", n);
    for (unsigned int i = 0; i < n; i++)
    {
        scanf("%d", &tab[i]);
    }

    int zero_cpt = 0;

    for (unsigned int i = 0; i < n; i++)
    {
        if (tab[i] == 0)
        {
            zero_cpt++;
        }
    }
    printf("Nombre d'entiers nuls : %d\n", zero_cpt);

    printf("Nombres pairs : ");
    for (unsigned int i = 0; i < n; i++)
    {
        if (tab[i] != 0 && tab[i] % 2 == 0)
        {
            printf("%d ", tab[i]);
        }
    }
    printf("\n");

    printf("Nombres impairs : ");
    for (unsigned int i = 0; i < n; i++)
    {
        if (tab[i] % 2 != 0)
        {
            printf("%d ", tab[i]);
        }
    }
    printf("\n");

    free(tab);
    return 0;
}


int main(void) {
  unsigned int n;
  printf("Entrez la taille de la table :\n");
  scanf("%u", &n);
  allocation(n);

  return 0;
}
