#include <stdio.h>
#include <string.h>

void echanger(char *c1, char *c2) {
  char *tmp = c1;
  c1 = c2;
  c2 = tmp;
}

void echanger_xor(char *c1, char *c2) {
if (*c1 != *c2) {
    *c1 = *c2 ^ *c1;
    *c2 = *c1 ^ *c2;
    *c1 = *c2 ^ *c1;
  }
}

void inverser(char *tab) {
  int n = strlen(tab);
  for(int i = 0; i < n / 2; i++) {
    echanger(&tab[i], &tab[n - i - 1]);
  }
}

void inverser_sans_variables(char *tab) {
  int *end = tab + (strlen(tab) - 1);
  while (tab < end) {
    echanger(tab, end);
    tab++;
    end--;
  }
}

int main(void) {
  char a = 'a';
  char b = 'b';
  echanger_xor(&a, &b);
  printf("%c\n", a);
  printf("%c\n", b);
}
