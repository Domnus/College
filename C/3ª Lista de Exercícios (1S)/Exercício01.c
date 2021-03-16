#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int num, quadrado;
    double raiz;
    printf("Digite um número: ");
    scanf("%d", &num);

    if(num > 0){
        quadrado = num * num;
        raiz = sqrt(num);
        printf("O quadrado de %d é %d. \nA raíz quadrada de %d é %lf.\n", num, quadrado, num, raiz);
    }
}