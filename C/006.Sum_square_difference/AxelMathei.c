// Euler 06

#include <stdio.h>

int main() {
    const int LIMIT = 100;
    int sum = LIMIT * (LIMIT + 1) / 2;
    int sum_sq = (2 * LIMIT + 1) * (LIMIT + 1) * LIMIT / 6;
    printf("%d", sum * sum - sum_sq);
}
