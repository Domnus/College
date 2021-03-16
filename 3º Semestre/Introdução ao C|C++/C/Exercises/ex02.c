#include <stdio.h>

int main() {
    int a, vet[50];

    scanf("%d", &vet[25]);

    a = *(vet+25);

    printf("vet[25]: %d ", a);

    return 0;
}

