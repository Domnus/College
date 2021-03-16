#include <stdio.h>

int main()
{
    int n;
    float i, numHarmonico = 0;
    printf("Digite um número: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        numHarmonico += 1 / i; 
    }
    printf("O número harmônico de %d é %f.\n", n, numHarmonico);
}