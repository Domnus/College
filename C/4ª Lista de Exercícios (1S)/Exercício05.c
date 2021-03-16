#include <stdio.h>

int main()
{
    int par = 0, impar = 0, num, i;
    int soma_par = 0, soma_impar = 0;
    float media_par, media_impar;
    printf("Digite o número desejado: \n");
    for (i = 0; i < 10; i++)
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
    
    media_impar = soma_impar / impar;
    media_par = soma_par / par;

    printf("A média dos números pares é %g.\n", media_par);
    printf("A média dos números ímpares é %g.\n", media_impar);

}