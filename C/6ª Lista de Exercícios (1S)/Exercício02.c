#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int upper = 50, lower = 1, i, num;
    float par = 0, soma = 0, media;
    
    for (i = 0; i < 20; i++) 
    {
        num = rand() % (upper - lower + 1) + lower;

        if (num % 2 == 0)
        {
            soma += num;
            par++;
        }
        printf("%d \n", num);
    } 
    
    media = soma / par;
    printf("A média é %.2f.\n", media);
}