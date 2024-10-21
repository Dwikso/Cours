#include <stdio.h>

int somme(int a) {
  unsigned int n , res = 0;
  scanf("%x", &n);
  while (n != 0) {
    res += n % 10;
    n /= 10;
  }
  printf("%d\n", res);
}

int main(void) {
  int annee = 1800;
  while(annee <= 2014) {
    int age = 2014 - annee;
    if (age == somme(annee)) {
      printf("\nL'age de Valentin est %d\n", age);

}
