#include <stdio.h>

int main()
{
    int N, fact = 1, i;

    printf("Digite um número:");
    scanf("%d", &N);

    for (i = N; i > 0; i--)
    {
        fact = fact * i;
    }
    printf("%d\n", fact);
}