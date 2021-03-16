#include <stdio.h>
#include <stdlib.h>

int main()
{

    int metros, milimetros;

    printf("Digite o valor em metros: ");
    scanf("%d", &metros);

    milimetros = metros * 100;

    printf("%d metro(s) é igual a %d milimetros.\n", metros, milimetros);

}