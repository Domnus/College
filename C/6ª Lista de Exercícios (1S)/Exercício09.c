#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int list[10];
    int upper = 50, lower = 1, n, i;

    while (i < 10)
    {
        n = rand() % (upper - lower + 1) + lower;
        for (int j = 0; j < 10; j++)
        {
            if (n == list[j])
            {
                break;
            }
            else
            {
                list[i] = n;
                i++;
            }
            
        }
    }

    for (i = 0; i < 10; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");
}