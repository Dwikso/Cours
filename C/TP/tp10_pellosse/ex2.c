#include <stdio.h>
#include <string.h>

int nbre_mot_de_taille_n(char *ch, int n) {
  int cpt = 0;
  int i = 0;
  int start = 0;

  int len = strlen(ch);

  while (i < len) {
    while (i < len && ch[i] == ' ') {
      i++;
    }
    start = i;
    while (i < len && ch[i] != ' ') {
      i++;
    }
    if (i > start) {
      int word_len = i - start;
      if (word_len == n) {
        cpt++;
      }
    }
  }
  return cpt;
}

int main(void) {
  char *ch = "bonjour vous avez pris place dans le train le plus rapide du monde";
  printf("nbre_mot_de_taille_n(ch, 4) = %d\n", nbre_mot_de_taille_n(ch, 4));
  printf("nbre_mot_de_taille_n(ch, 7) = %d\n", nbre_mot_de_taille_n(ch, 7));
  printf("nbre_mot_de_taille_n(ch, 8) = %d\n", nbre_mot_de_taille_n(ch, 8));
  return 0;
}
