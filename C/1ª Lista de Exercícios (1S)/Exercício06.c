#include <stdio.h>

int main()
{

    float salario, porcentagem, total;

    printf("Digite o seu salário: ");
    scanf("%f", &salario);

    printf("Digite o percentual de reajuste: ");
    scanf("%f", &porcentagem);

    total = salario * (1 + (porcentagem / 100));

    printf("O salário final será: R$%f\n", total);

}