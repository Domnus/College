#include <stdio.h>

void dobro(int *a)
{
    *a += *a;
}

int main()
{
    int num;
    printf("Digite um número: ");
    scanf("%d", &num);

    dobro(&num);

    printf("O novo valor é: %d.\n", num);
}