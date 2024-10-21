#include <stdio.h>
#include <stdlib.h>


int main(void) {
  int nbre,i,n, cptnegs = 0, cptpos =0; 
  int *p;
  printf("Merci de rentrer le nombre de valeurs a lire : ");
  scanf("%d", &n);
  p = (int *) malloc(n * sizeof(int));
  if (p == NULL) {
    return 1;
  };
  for (i = 0; i < n; i++) {
    printf("\n Merci de rentrer de %deme nombre : ", i+1);
    scanf("%d", &nbre);
    * (p+i) = nbre;
    (nbre >=0)?cptpos++:cptnegs++;
    printf("\n Il y a %d nombre(s) positif(s) : ", cptpos);
    for(i=0; i <n; i++) {
      if (*(p+i) >= 0) {
        printf("%d \n", *(p+i));
    }
  }
}
}
