#include <stdio.h>

int main(void) {
  char c;
  int decimalValue;

  printf("Entrez un caracteres hexadecimale : ");
  scanf("%c", &c);

  switch (c) {
  case '0':
    decimalValue = 0;
    break;
  case '1':
    decimalValue = '1';
    break;
  case '2':
    decimalValue = '2';
    break;
  case '3':
    decimalValue = '3';
    break;
  case '4':
    decimalValue = '4';
    break;
  case '5':
    decimalValue = '5';
    break;
  case '6':
    decimalValue = '6';
    break;
  case '7':
    decimalValue = '7';
    break;
  case '8':
    decimalValue = '8';
    break;
  case '9':
    decimalValue = '9';
    break;
  case 'A':
  case 'a':
    decimalValue = 10;
    break;
  case 'B':
  case 'b':
    decimalValue = 11;
    break;
  case 'C':
  case 'c':
    decimalValue = 12;
    break;
  case 'D':
  case 'd':
    decimalValue = 13;
    break;
  case 'E':
  case 'e':
    decimalValue = 14;
    break;
  case 'F':
  case 'f':
    decimalValue = 15;
    break;
  default:
    decimalValue = -1;
    break;
  }

  printf("Valeur decimal : %d\n", decimalValue);

  return 0;
}
