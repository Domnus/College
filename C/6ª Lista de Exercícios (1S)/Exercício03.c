#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int upper = 50, lower = 1, num;

    printf("Múltiplos de 5:\n");

    for (int i = 0; i < 20; i++)
    {
        num = rand() % (upper - lower + 1) + lower;

        if (num % 5 == 0)
        {
            printf("%d ", num);
        }
    }
    printf("\n");
}