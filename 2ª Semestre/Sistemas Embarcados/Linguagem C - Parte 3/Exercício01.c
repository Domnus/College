#include <stdio.h>

int parOuImpar(int num)
{
    if (num % 2 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int n;
    printf("Digite um número: ");
    scanf("%d", &n);

    if (parOuImpar(n))
    {
        printf("Número par.\n");
    }
    else
    {
        printf("Número impar.\n");
    }
    
}
