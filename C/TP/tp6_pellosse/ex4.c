#include <stdio.h>

int absolu(int a) {
  printf("Addresse du paramètres a : %p\n", &a);
  printf("Valeur initial du paramètres a : %d\n", a);
  if (a < 0) {
    return -a;
  } else {
    return a;
  }
}


int main(void) {
  int absolu (int a);
  int i =- 20;
  printf("Addresse de i : %p\n", &i);
  printf("La valeur absolue de i est : %d.\n", absolu(i));
  return 0;
}
