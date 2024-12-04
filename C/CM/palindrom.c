#include <stdio.h>

int palindrom(char *s, int debut, int fin) {
  int i=debut, j=fin;
  while (i<j) {
    if (s[i] != s[j]) return 0;                                                                                   <
    i++;
    j--;
  }
  return 1;
FDS
*
