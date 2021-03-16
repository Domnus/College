//Cálculo de raízes de equações do segundo grau, quer sejam reais ou complexas

#include <math.h>
#include <stdio.h>

int main()
{
    float a, b, c, delta, raiz_delta;

    printf("\nBHASKARA\n\n");

    printf("\nDigite o valor de A: ");
    scanf("%f", &a);
    printf("\nDigite o valor de B: ");
    scanf("%f", &b);
    printf("\nDigite o valor de C : ");
    scanf("%f", &c);

    delta = (pow(b, 2) - 4*a*c);

    if(delta >= 0)
    {
        if(delta == 0)
        {
            printf("\nA raiz x1 = %f", ((-b + sqrt(delta))/2*a));
        }

        else
        {
            printf("\nA raiz x1 = %f", ((-b + sqrt(delta))/2*a));
            printf("\nA raiz x2 = %f", ((-b - sqrt(delta))/2*a));
        }
    }

    else
    {
        delta = fabs(delta);
        raiz_delta = sqrt(delta);

        printf("\nA raiz x1 = %f + %fi", ((-b)/2*a), ((raiz_delta)/2*a));
        printf("\nA raiz x2 = %f - %fi", ((-b)/2*a), ((raiz_delta)/2*a));
    }

    return(0);
}