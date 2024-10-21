#include <stdio.h>

int puissance_l (int a, int b) {
    int result = a;
    for (int i = 1; i < b; i++) {
        result = result * a;
    }
    return result;
}

int puissance_r (int a, int b) {
    int t = puissance_r(a,b/2);
    if (b == 0) return 1;
    if (b % 2 == 0) {
        return t*t;
    } else {
        return a * puissance_r(a, b-1);
    }
}

int main(void) {
  int a,b;
  printf("Donnez d'eux nombres :  ");
  scanf("%d %d",&a,&b);
  printf("Puissance de %d à la %d : %d\n",a,b,puissance_r(a,b));
}
