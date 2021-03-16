#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n1, n2, resultado;
    printf("Digite o primeiro número: ");
    scanf("%d", &n1);
    printf("Digite o segundo número: ");
    scanf("%d", &n2);
    resultado = n1 + n2;
    printf("A soma de %d + %d é igual a %d.\n", n1, n2, resultado);
    
}