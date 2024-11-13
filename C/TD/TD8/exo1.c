#include <stdio.h>
#include <stdlib.h>
#define k 3

int est_carre_magique(int tab[k][k])
{
    int res = 0, res2 = 0;
    for (int i = 0; i < k; i++)
    {
        res += tab[i][i];
    }
    for (int i = 0; i < k; i++)
    {
        res2 += tab[i][k - 1 - i];
    }
    if (res != res2)
        return 0;

    for (int i = 0; i < k; i++)
    {
        int ligRes = 0, colRes = 0;
        for (int j = 0; j < k; j++)
        {
            ligRes += tab[i][j];
            colRes += tab[j][i];
        }
        if (ligRes != res || colRes != res)
            return 0;
    }
    return 1;
}

int main()
{
    int tab[k][k] = {
        {8, 1, 6},
        {3, 5, 7},
        {4, 9, 2}};

    if (est_carre_magique(tab))
        printf("Le tableau est un carré magique.\n");
    else
        printf("Le tableau n'est pas un carré magique.\n");

    return 0;
}
