#include <stdio.h>

int main()
{

    int l1, l2, l3;

    printf("Lado 1: ");
    scanf("%d", &l1);
    
    printf("Lado 2: ");
    scanf("%d", &l2);

    printf("Lado 3: ");
    scanf("%d", &l3);

    if ((l1 +l2) < l3 || (l1 + l3) < l2 || (l2 + l3) < l1){
        printf("Não é um triângulo\n");
    }
    else if (l1==l2 && l2==l3){
        printf("É um triângulo equilátero.\n");
    }
    else if (l1==l2 || l1==l3 || l2==l3){
        printf("É um triângulo isósceles.\n");
    }
    else{
        printf("É um triângulo escaleno.\n");
    }
}