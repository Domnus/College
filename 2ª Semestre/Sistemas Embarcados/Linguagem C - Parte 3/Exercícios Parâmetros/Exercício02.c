#include <stdio.h>

float maiorEMedia(float a, float b, float *m)
{
    *m = (a + b) / 2;

    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
    
}

int main()
{
    float n1, n2, media = 0, maior;

    printf("Digite duas notas separadas por um espaço: ");
    scanf("%f %f", &n1, &n2);

    maiorEMedia(n1, n2, &media);
    maior = maiorEMedia(n1, n2, &media);

    printf("A maior nota é %g e a média é %g.\n", maior, media);
}