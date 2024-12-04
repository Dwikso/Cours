#include <stdio.h>

int majuscule(const char c) {
  if (c >='A' && c <= 'Z') {
    return 1;
  } else {
    return 0;
  }
}

int compte_majuscule(const char *s) {
  int count = 0;
  while(*s) {
    if(majuscule(*s)) {
      count++;
    }
    s++;
  }
  return count;
}

int main(void) {
  const char *str = "Hello World!";
  printf("%d \n", compte_majuscule(str));
  return 0;
}
