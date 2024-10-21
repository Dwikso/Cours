#include <stdio.h>

int puissance_r (int a, int b) {
    if (b == 0) return 1;
    if (b % 2 == 0) {
        return puissance_r(a, b/2) * puissance_r(a, b/2);
    } else {
        return a * puissance_r(a, b-1);
    }
}
