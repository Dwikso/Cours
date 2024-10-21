#include <stdio.h>

int main(void) {
  char car;
  printf("\nMerci d'introduire une lettre majuscule ou minuscule: ");
  scanf("%c", &car);
  printf("\nla conversion (majuscule vs minuscule) de %c donne %c.\n",car,car + (car < 'a' ? 'a'-'A' : 'A' -'a'));
  return 0;

}
