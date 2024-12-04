#include <stdio.h>

int main(void) {
  int t[3] = {10, -20, 320};
  printf("les addresses de t et de t+1 sont : %p et %p \n", &t, &t+1);
  printf("les addresses de t[0] et t[0] + 1 sont : %p et %p \n", &t[0], &t[0] + 1);
  printf("les valeurs de t et t+1 sont : %p et %p \n", t, t+1);
  return 0;
}

// Chaque valeurs dans le tableau sont différentes
