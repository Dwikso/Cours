#include <stdio.h>

int entier_palindrome(int n) {
  int n1 = n;
  int n2 = 0;
  while (n1 > 0) {
    n2 = n2 * 10 + n1 % 10;
    n1 = n1 / 10;
  }
  return n == n2;
}

int main() {
  int n;
  scanf("%d", &n);
  if (entier_palindrome(n)) {
    printf("1\n");
  } else {
    printf("0\n");
  }
  return 0;
}
