#include <stdio.h>

/* int main(void) { */
/*   unsigned short int n, res = 0; */
/*   scanf("%hu", &n); */
/*   for (int a = 0; a < n; a += 2) { */
/*     res += a; */
/*   } */
/*   printf("%d \n", res); */
/* } */

int main(void) {
  int n, i, somme = 0;
  do {
    printf("\n Merci d'introduire un nombre strictement positfif :");
    scanf("%d", &n);
  } while (n <= 0);
}

