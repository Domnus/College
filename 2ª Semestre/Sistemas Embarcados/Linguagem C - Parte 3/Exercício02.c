#include <stdio.h>

int maior(int a, int b, int c)
{
    if (a > b && a > c)
    {
        return a;
    }
    else if (b > a && b > c)
    {
        return b;
    }
    else
    {
        return c;
    }
    
}

int main()
{
    int a,b,c;
    printf("Digite 3 números separados por um espaço: ");
    scanf("%d %d %d", &a, &b, &c);

    printf("O maior número é %d.\n", maior(a,b,c));
    
}