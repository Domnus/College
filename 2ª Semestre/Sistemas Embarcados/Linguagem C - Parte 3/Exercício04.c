#include <stdio.h>
#include <stdbool.h>

int operacao(int num1, int num2, char operador)
{
    if (operador == '+')
    {
        return num1 + num2;
    }
    if (operador == '-')
    {
        return num1 - num2;
    }
    if (operador == '*')
    {
        return num1 * num2;
    }
    if (operador == '/')
    {
        return num1 / num2;
    }
    else
    {
        return false;
    }

}

int main()
{
    int num1, num2, op, result;
    printf("Digite uma operação: ");
    scanf("%d%c%d", &num1, &op, &num2);

    result = operacao(num1, num2, op);
    if (result == 0)
    {
        printf("Operação inválida!\n");
    }
    else
    {
        printf("O resultado é %d.\n", result);
    }
}
