#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int SIZE = 12;
    for (int i = 0; i < 12; i++) {
        printf("%d ", fibonacci(i));
    }
   return 1;
}
