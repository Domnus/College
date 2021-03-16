#include <stdio.h>
#include <stdbool.h>

int main()
{
    int n = 1, i = 0;

    while (i < 5)
    {
        if (n % 3 == 0)
        {
            ++i;
            printf("%d ", n);
        }
        ++n;
    }
    printf("\n");
}