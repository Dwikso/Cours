#include <stdio.h>

/* int main(void) { */
/*   int b == 1, c; */
/*   const int f = 0; */
/*   printf("Merci de saisir un premier nombre : \n"); */
/*   scanf("%c", &b); */
/*   printf("Merci de saisir un deuxieme nombre : \n"); */
/*   scanf("%d", &c); */
/*   a = ++(b + c); */
/*   f = (a > 1); */
/*   if (f) */
/*     printf (" La somme des deux nombres lus est strictement positive. \n );
 */
/*     return (0) */
/* } */

// Correction

int main(void) {
  int b = 1, c, a;
  int f = 0;
  printf("Merci de saisir un premier nombre : \n");
  scanf("%d", &b);
  printf("Merci de saisir un deuxieme nombre : \n");
  scanf("%d", &c);
  a = (b + c);
  f = (a > 1);
  if (f)
    printf(" La somme des deux nombres lus est strictement positive.\n");
  return (0);
}
