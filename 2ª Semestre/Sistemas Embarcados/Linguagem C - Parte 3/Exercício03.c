#include <stdio.h>

int qAlgs(int n)
{
    int  countDigits = 0, valor = 1;

    while (valor <= n)
    {
        valor *= 10;
        countDigits++;
    }
    return countDigits;
}

int main()
{
    int num, algs;

    printf("Digite um número: ");
    scanf("%d", &num);

    algs = qAlgs(num);

    printf("O número %d tem %d dígitos.\n", num, algs);
}