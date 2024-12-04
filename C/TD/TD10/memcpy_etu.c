#include <stdio.h>

void * memcpy_etu(void *destination, const void *source, size_t n) {
  char *a = (char *)destination;
  char *b = (char *)source;
  for(int i = 0; i < n; i++) {
    a[i] = b[i]
  }
}

int main(void) {
  
}
