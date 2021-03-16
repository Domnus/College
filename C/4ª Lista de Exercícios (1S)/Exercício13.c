#include <stdio.h>

int main()
{
    int num, i, flag = 0;

    printf("Digite um número: ");
    scanf("%d", &num);

    if (num > 1)
    {
        for (i = 2; i <= num / 2; ++i)
        {
            if (num % i == 0)
            {
                flag = 1;
                break;
            }
        }
    }

    if (flag == 1)
    {
        printf("Não é primo.\n");
    }
    else
    {
        printf("É primo.\n");
    }
}