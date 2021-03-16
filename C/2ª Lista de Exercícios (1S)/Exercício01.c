#include <stdio.h>

int main()
{

    int num, c, d, u;

    printf("Digite um número: ");
    scanf("%d", &num);

    u = num / 100;
    d = (num / 10) % 10;
    c = num % 10;

    if (num >= 100 && num < 1000) {
        if (c > d && d > u) {
            printf("%d é ascendente.\n", num);
        }
        else {
            printf("%d não é ascendente.\n", num);
        }
    }
    else {
        printf("Número inválido!\n");
    }
}