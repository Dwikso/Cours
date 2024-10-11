```c
#include <stdio.h>

int main(void) {
  unsigned char i;
  i = 250;
  i = i + 6;
  printf("La valeur de i est %d \n", i);
  return 0;
}
```

```console
La valeur de i est 0 car i est assigné a un unsigned char donc quand on ajoute 6 à i, il revient a 0 .
```
