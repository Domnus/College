#include <stdio.h>

int main()
{
    int i = 1000;

    while (i >= 199)
    {
        printf("%d ", i);
        i -= 3;
    }
}