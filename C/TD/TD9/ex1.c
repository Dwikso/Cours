#include <stdio.h>
#include <string.h>


int voyelle(const char c) {
  char voyelles[6] = {'a','e','i','o','u','y'};
  int i;
  for(i=0; i < 6; i++) {
    if (voyelles[i] == c) return 1;
  }
  return 0;
}


int main(void) {
  printf("%d \n",voyelle('e'));
  return 0;
}
