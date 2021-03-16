#include <stdio.h>

int main()
{
    int valor; 
    
    printf("Valor de bits a ser trocado: B$");
    scanf("%d", &valor);

    int n50 = valor / 50;
    int n10 = valor % 50 / 10;
    int n5 = valor % 50 % 10 / 5;
    int n1 = valor % 50 % 10 % 5;

    printf("O valor de B$%d será trocado por ", valor);
    if (n50 > 0)
    {
        printf("%d notas de B$50 ", n50);
    }
    if (n10 > 0)
    {
        printf("%d notas de B$10 ", n10);
    }
    if (n5 > 0)
    {
        printf("%d notas de B$5 ", n5);
    }
    if (n1 > 0)
    {
        printf("%d notas de B$1.\n", n1);
    }
    
    
}