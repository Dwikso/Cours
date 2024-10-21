#include <stdio.h>

#define k 10

int tous_diff(unsigned int *t) {
  for(int i = 0; i < k -1; i++) {
    for (int j= i +1;j < k; j++) {
      if(t[i] == t[j]){
        return 0;
      }
    }
  }
  return 1;
}

int main(void) {
  unsigned int t[] = {10,25,7,48, 3, 1, 100, 85, 11, 22}
  printf("%d\n", tous_diff(t));
  return 0;
}
