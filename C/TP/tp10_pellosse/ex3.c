#include <stdio.h>
#include <string.h>

const char *strstr_fin( const char * grande, const char * petite) {
  char *p = NULL;
  char *c = strstr(grande, petite);
  while (c != NULL) {
    p = c;
    c = strstr(c + 1, petite);
  }
  return p;
}

int main(void) {
  char *ch = "bonjour le monde vous avez pris place dans le train le plus rapide du monde test";
  printf("strstr_fin(ch, mondeé) = %s\n", strstr_fin(ch, "monde"));
  return 0;
}
