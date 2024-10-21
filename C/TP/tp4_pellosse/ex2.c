#include <stdio.h>

int main(void) {
  int *p=(int *) 0x100a;
  double *p1=(double *) 0x200b;
  printf("%d \n", sizeof(p1) > sizeof(p));
  printf("%p \n",p+1);
  printf("%p \n",p1+1);
  return 0;
}

// Le programme affiche :
// 0 
// 0x100e 
// 0x2013
