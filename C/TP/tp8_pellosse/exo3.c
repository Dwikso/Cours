#include <stdio.h>
#include <stdlib.h>

int egale(int a, int b) {
  if (a > b) return 1;
  else if (a == b) return 0;
  else return -1;
}

int egale2(unsigned int a, unsigned int b) {
  unsigned int Sa, Sb;
  while (a && b) {
    Sa = a;
    Sb = b;
    while (Sa && Sb) {
      Sa = Sa >> 1;
      Sb = Sb >> 1;
    }
    if (Sa) return 1;
    else if (Sb) return -1;
    a = a << 1;
    b = b << 1;
  }
  return 0;
}


int main(void) {
  int a = 5;
  int b = 5;
  if (egale2(a, b) == 1) {
      printf("a est strictement plus grand que b sans les comparaisons.\n");
  } else if (egale2(a, b) == -1) {
        printf("a est strictement plus petit que b sans les comparaisons.\n");
  } else {
        printf("a est égal à b sans les comparaisons.\n");
  }
}
