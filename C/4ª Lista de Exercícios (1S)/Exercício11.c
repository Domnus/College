#include <stdio.h>

int main()
{
    int num, n1, n2, s;

    for (num = 1000; num < 10000; num++)
    {
        n1 = num / 100;
        n2 = num % 100;
        s = n1 + n2;

        if ((s * s) == (num))
        {
            printf("%d\n", num);
        }
    }
}