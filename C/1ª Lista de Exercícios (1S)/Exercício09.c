#include <stdio.h>

int main()
{

    float f, c;

    printf("Fahrenheit: ");
    scanf("%f", &f);

    c = ((f - 32)/9) * 5;

    printf("%fºF = %fCº\n", f, c);

}