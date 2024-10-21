```c
#include <stdio.h>

int main(void) {
  printf("%cn Impression avec les codes ASCII ... %cn", 92, 92);
  return 0;
}
```

L'étudiant a utiliser le code ASCII 92 pour imprimer le caractère `\` et le code

Le code ne fonctionne pas correcement car il a afficher le caractère `\` et le caractère `\` au lieu de `\n` pour pouvoir faire un retour a la ligne
