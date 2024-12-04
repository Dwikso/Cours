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

int compte_voyelles(const char *s) {
  if (*s == '\0') return 0;
  if (voyelle(s[0]) return compte_voyelles((s+1));
  else return compte_voyelles((s+1));
}

int main(void) {
  printf("%d", compte_voyelles('Bonjour'));
}
