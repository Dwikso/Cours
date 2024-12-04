#include <stdio.h>
#include <string.h>

int toutes_lettres_differentes(char *s) {
  int i,j;
  for(i = 0; s[i] != '\0'; i++) {
    for(j = i + 1; s[i] != '\0'; j++) {
      if (s[i] != s[j]) {
        return 1;
      }
    }
  }
  return 0;
}

int main(void) {
  char mot[4] = "lens";
  printf("%d \n", toutes_lettres_differentes(mot));
  return 0;
}
