#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define taille 10

int comparer_chaine(const char *s1, const char *s2) {
  while (*s1 && *s2) {
    if (*s1 < *s2) {
      return -1;
    } else if (*s1 > *s2) {
      return 1;
    }
    s1++;
    s2++;
  }

  if (*s1 == '\0' && *s2 == '\0') {
    return 0;
  } else if (*s1 == '\0') {
    return -1;
  } else {
    return 1;
  }
}

int main(void) {
    const char *s1 = "Lens";
    const char *s2 = "Lens";

    int result = comparer_chaine(s1, s2);

    if (result == -1) {
        printf("'%s' est strictement inférieur à '%s'\n", s1, s2);
    } else if (result == 0) {
        printf("'%s' est égal à '%s'\n", s1, s2);
    } else {
        printf("'%s' est strictement supérieur à '%s'\n", s1, s2);
    }

    return 0;
}

