#include <stdio.h>

int main()
{
    float sal, empr;

    printf("Digite o salário: ");
    scanf("%f", &sal);

    printf("Digite o valor da prestação do empréstimo: ");
    scanf("%f", &empr);

    if (sal * 0.2 > empr)
    {
        printf("Empréstimo concedido.\n");
    }
    else
    {
        printf("Empréstimo não concedido.\n");
    }
}