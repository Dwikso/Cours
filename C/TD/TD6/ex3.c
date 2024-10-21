#include <stdio.h>
#include <stdilib.h>

int f(int *a, int n) {
  if (n==1) return 1;
  if(a[0] > a[1]) return 0;
  else {
    return f(a+1, n-1)
  }
}

int main(void) {
  int *tab;
  int n,i;
  scanf("%d", n);
  tab=(int*)malloc(n*sizeof(int));
  for(i=0;i < n;i++) {
    scanf("%d", tab+i);
  }
  if(f(tab,n)) printf("Tab Triée");
  else printf("Tab non triée"){
    return 0;
  }
}
