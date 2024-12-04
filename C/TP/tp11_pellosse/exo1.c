#include <stdio.h>
#include <string.h>


float copier_un_reel_v1(float b) {
  float a;
  memcpy(&a, &b, sizeof(b));
  return a;
}

void copier_un_reel_v2(float *a, float b) {
  memcpy(a, &b, sizeof(b));
}

void copier_un_reel_v3(float *a, float *b) {
  memcpy(a,b,sizeof(float));
}

void copier_un_tableau(int a[], int b[], int n) {
  memcpy(a,b,n * sizeof(int))
}

void * memcpy_etu(void *destination, const void *source, size_t n) {
  char *a = (char *)destination;
  char *b = (char *)source;
  for(int i = 0; i < n; i++) {
    a[i] = b[i]
  }
}