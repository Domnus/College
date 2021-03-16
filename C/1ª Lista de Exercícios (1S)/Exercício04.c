#include <stdio.h>

int main()
{

    int dias, horas, minutos, segundos, total;

    printf("Digite o total de dias: ");
    scanf("%d", &dias);

    printf("Digite o total de horas: ");
    scanf("%d", &horas);

    printf("Digite o total de minutos: ");
    scanf("%d", &minutos);

    printf("Digite o total de segundos: ");
    scanf("%d", &segundos);

    total = segundos + (minutos * 60) + (horas * 3600) + (dias * 24 * 3600);

    printf("Total de segundos: %d\n", total);

}