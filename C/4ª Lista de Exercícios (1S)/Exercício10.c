#include <stdio.h>
#include <ctype.h>

int main()
{
    int s1, s2, soma;
    char v;

    while (v != 'Z')
    {
        printf("1º número: ");
        scanf("%d", &s1);
        printf("2º número: ");
        scanf("%d", &s2);

        if (s1 > s2)
        {
            printf("O primeiro número deverá ser menor que o segundo!\n");
            continue;
        }
        else
        {
            soma = s1 + s2;
            printf("A soma é igual a %d.\n", soma);
        }

        printf("Digite Z para parar o programa.\n");
        printf("-> ");
        scanf("%s", &v);
        v = toupper(v);
    }
}