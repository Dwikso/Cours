#include <stdio.h>
/* int main(void) { */
/*   int i = 5, j = 2; */
/*   float f; */
/*   f = 4 * (i / j); */
/*   printf(" La valeur de f est : %.f .\n", f); */
/*   return (0); */
/* } */

/* int main(void) { */
/*   int i = 5, j = 2; */
/*   float f; */
/*   f = 4 * (float)(i / j); */
/*   printf("La Valeur de f, après une application globale de l'opérateur cast,
 * " */
/*          "est : %f. \n", */
/*          f); */
/*   return (0); */
/* } */

int main(void) {
  int i = 5, j = 2;
  float f;
  f = 4 * ((float)i / (float)j);
  printf("La valeur de f , après des application locaux de l' "
         "opérateur cast , est :%f .\n ",
         f);
  return (0);
}
