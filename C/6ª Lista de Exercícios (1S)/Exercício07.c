#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int list[10];
    int upper = 50, lower = 1, n;

    for (int i = 0; i < 10; i++)
    {
        list[i] = rand() % (upper - lower + 1) + lower;
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = i + 1; j < 10; j++)
        {
            if (list[i] > list[j])
            {
                n = list[i];
                list[i] = list[j];
                list[j] = n;
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", list[i]);
    }
    printf("\n");

}