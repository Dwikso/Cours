#include <stdio.h> 

/* int abs(int a) */
/* { */
/*   if (a < 0) */
/*     return -a; */
/*   return a; */
/* } */

/* int main(void) */
/* { */
/*   int a; */
/*   scanf("%d", &a); */
/*   printf("%d\n", abs(a)); */
/* } */

int max(int a, int b)
{
  if (a > b)
    return a;
  return b;
}

int main(void)
{
  int a, b;
  scanf("%d %d", &a, &b);
  printf("%d\n", max(a, b));
}
