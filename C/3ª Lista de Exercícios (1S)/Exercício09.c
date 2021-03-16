#include <stdio.h>

int main()
{
    int farinha, ovos, leite;
    float A, B, C;

    printf("Farinha: ");
    scanf("%d", &farinha);

    printf("Ovos: ");
    scanf("%d", &ovos);

    printf("Leite: ");
    scanf("%d", &leite);

    A = farinha / 2;
    B = ovos / 3;
    C = leite / 5;

    if (A <= B && A <= C)
    {
        printf("Será possível fazer %g bolos.\n", A);
    }
    else if (B <= C && B<= A)
    {
        printf("Será possível fazer %g bolos.\n", B);
    }
    else 
    {
        printf("Será possível fazer %g bolos.\n", C);
}