#include <stdio.h>

int main()
{

    float preco, desempenho, distancia;
    float litros, dindin;

    printf("Preço do combustível [R$]: ");
    scanf("%f", &preco);

    printf("Desempenho do veículo [Km/L]: ");
    scanf("%f", &desempenho);

    printf("Distância entre as cidades [Km]: ");
    scanf("%f", &distancia);

    litros = desempenho * distancia;
    dindin = litros * preco;

    printf("Uma viagem de %f km gastará %f litros e custará R$%f\n", distancia, litros, dindin);

}