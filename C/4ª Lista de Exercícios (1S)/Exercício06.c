#include <stdio.h>

int main()
{
    int par = 0, impar = 0, num, i, n;
    int soma_par = 0, soma_impar = 0;
    float media_par, media_impar;

    printf("Digite a quantidade de números: ");
    scanf("%d", &n);

    printf("Digite as notas: \n");
    for (i = 0; i < n; i++)
    {
        printf("-> ");
        scanf("%d", &num);

        if (num % 2 == 0)
        {
            par++;
            soma_par += num;
        }
        else
        {
            impar++;
            soma_impar += num;
        }
    }
    media_par = soma_par / par;
    media_impar = soma_impar / par;

     printf("A média dos números pares é %g.\n", media_par);
    printf("A média dos números ímpares é %g.\n", media_impar);
}