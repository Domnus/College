#include <stdio.h>

int main()
{

    float kmPercorridos, qDias, aPagar;

    printf("Km Percorridos: ");
    scanf("%f", &kmPercorridos);

    printf("Dias que o carro foi alugado: ");
    scanf("%f", &qDias);

    aPagar = (kmPercorridos * 0,15) + (qDias * 60);

    printf("Total a pagar: R$%f\n", aPagar);

}