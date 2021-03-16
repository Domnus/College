#include <stdio.h>

int main()
{
    float s = 0, n = 1, i = 1;

    while (i < 51 || n < 100)
    {
        s += n / i;
        n += 2;
        i++;
    }

    printf("%f\n", s);
    return 0;
}
