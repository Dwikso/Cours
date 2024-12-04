#include <stdio.h>
#include <stdlib.h>

#define k 3

struct _coordonees {
  int x;
  int y;
};

typedef struct _coordonees coordonees;

void position (int tab[][k], int nbre, struct _coordonees *pos) {
  int i,j,trouve = 0;
  for(i=0; i <k; i++) {
    for(j=0; j <k; j++) {
      if(tab[i][j] == nbre) {
        pos->x = i;
        pos->y = j;
        trouve = 1;
      }

    }
  }
  if(!trouve) {
    pos->x = -1;
    pos->y = -1;
  }
}

int main(void) {
  coordonees c;
  int tab[k][k] = {{1,2,3},{4,5,6},{7,8,9}};
  printf("Entrez un nombre : ");
  scanf("%d",&c);
  if(c.x == - 1) {
    printf("Le nombre %d n'existe pas\n",c);
  } else {
    printf("Le nombre %d est à la position (%d,%d)\n",c,c.x,c.y);
  }
}

