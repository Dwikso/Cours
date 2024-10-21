#include <stdio.h>

int main(void)
{
  int i = 1;
  int *p1, *p2;
  p1 = &i;
  p2  = p1;
  *p2 += 3;
  printf("La valeur de i : %d \n", i);
  return 0;
}
