#include <stdio.h>

int main()
{
    int a = 0, b = 5.8;

    if (b <= 10) {
        a += 5;
    }
    printf("Valores a = %d e b = %d", a, b);

    return(0);
}