#include <stdio.h>

int main()
{
    int dia, mes, ano;

    printf("Dia: ");
    scanf("%d", &dia);

    printf("Mês: ");
    scanf("%d", &mes);

    printf("Ano: ");
    scanf("%d", &ano);

    if (mes > 12 || mes < 0)
    {
        printf("Data inválida!\n");
    }
    else if (dia < 1 || dia > 31)
    {
        printf("Data inválida!\n");
    }
    else if ((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0))
    {
        if (mes = 2 && dia > 29)
        {
            printf("Data inválida!\n");
        }
        else
        {
            printf("Data válida!\n");
        }
    }
    else if (mes = 2 && dia > 28)
    {
        printf("Data inválida!\n");
    }
    else
    {
        printf("Data válida!\n");
    }
}
