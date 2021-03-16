#include <stdio.h>

int main()
{
    int soma= 0, i = 0, x = 2;

    while (i < 50)
    {
        if (x % 2 == 0)
        {
            soma += x;
            i++;
        }
        x++;
    }
    printf("A soma dos primeiros 50 números pares é %d.\n", soma);
}