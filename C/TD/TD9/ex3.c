#include <stdio.h>
#include <string.h>

#define t 22

int dora(int *pp) {
  int i = 0;
  int k = t;
  while (pp[i] != 1) && (t!=0) {
    if (pp[i] < t) t -= p[i];
    i++;
  }
  if (t == 0) {
    i = 0;
    while (k != 0) {
      if (pp[i] < k) {
        k -= pp[i];
        printf("%d", pp[i]);
        i++;
      }
      return 1;
    }
  }
  return 0;
}
