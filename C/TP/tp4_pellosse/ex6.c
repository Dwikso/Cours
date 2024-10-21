#include <stdio.h>

void genererSousEnsembles(char *ensemble, int n)
{
    int total = 1 << n;

    printf("Les sous ensembles sont :\n");
    for (int i = 0; i < total; i++)
    {
        printf("{ ");
        int first = 1;  
        for (int j = 0; j < n; j++)
        {
            if (i & (1 << j))
            {
                if (!first)
                {
                    printf(", ");
                }
                printf("%c", ensemble[j]);
                first = 0;  
            }
        }
        printf(" }\n");
    }
}

int main(void)
{
    char ensemble[30];
    int n = 0;
    char lettres;

    printf("Entrez votre ensemble de lettres : {");

    while (1)
    {
        scanf("%c", &lettres);
        if (lettres == '}')
        {
            break;
        }
        if (lettres >= 'a' && lettres <= 'z')
        {
            ensemble[n++] = lettres;
        }
        else if (lettres == ',')
        {
            continue;
        }
    }
    ensemble[n] = '\0';

    genererSousEnsembles(ensemble, n);

    return 0;
}

