#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int upper = 50, lower = 1, num, n;

    printf("Insira um número: ");
    scanf("%d", &n);

    printf("Múltiplos de %d: ", n);
    
    for (int i = 0; i < 20; i++)
    {
        num = rand() % (upper - lower + 1) + lower;

        if (num % n == 0)
        {
            printf("%d ", num);
        }
    }
    printf("\n");
}