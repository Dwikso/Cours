#include <stdio.h>

int main(void) { 
  int i;
  for(i=0,printf("Instruction 1\n"); i!=5; i++, printf("Instruction 2\n")) {
    printf("La valeur de i est %d\n : ", i);
  }
  return 0;
}
