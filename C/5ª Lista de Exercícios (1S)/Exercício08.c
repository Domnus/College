#include <stdio.h>
#include <stdbool.h>

int main()
{
    int R, R1, R2;    

    while (true)
    {
        printf("R1: ");
        scanf("%d", &R1);

        if (R1 == 0)
        {
            printf("Programa parado pelo usuário.\n");
            break;
        }
        else
        {
            printf("R2: ");
            scanf("%d", &R2);
        
            if (R1 == 0 || R2 == 0)
            {
                printf("Programa parado pelo usuário.\n");
                break;
            }
            else
            {
                R = (R1*R2) / R1 + R2;
            }

            printf("O resultado da associação em paralelo é igual a %dΩ.\n", R);
        }    
    }    
    
}
