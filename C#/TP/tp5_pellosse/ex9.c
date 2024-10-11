#include <stdio.h>

void diviser(int p, int q, int precision) {
  float div = p / q;
  for(int i = 0; i < precision; i++) {
    while(i != precision) {
      i++;
      div *= 10;
    }
  }
  return div;
}

int main(void) {
  diviser(1, 97, 3);
  return 0;
}
