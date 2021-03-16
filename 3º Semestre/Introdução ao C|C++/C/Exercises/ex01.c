#include <stdio.h>

void troca(int *a, int *b) {
    int x = *a;
    *a = *b;
    *b = x;
}

int main() {
    int a, b;

    printf("a -> ");
    scanf("%d", &a);

    printf("b -> ");
    scanf("%d", &b);

    troca(&a, &b);

    printf("a: %d\nb: %d", a, b);

    return 0;
}