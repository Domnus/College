#include <stdio.h>

int main()
{
    float km, litros, consumo;

    printf("Distância [Km]: ");
    scanf("%f", &km);

    printf("Litros: ");
    scanf("%f", &litros);

    consumo = km / litros;

    if (consumo < 8)
    {
        printf("Venda o carro.\n");
    }
    else if (consumo >= 8 && consumo <= 14)
    {
        printf("Econômico.\n");
    }
    else
    {
        printf("Super econômico.\n");
    }
}