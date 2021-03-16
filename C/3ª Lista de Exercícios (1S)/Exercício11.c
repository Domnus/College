#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));
    int lower = 1, upper = 99;
    int a = (rand() % (upper - lower + 1) + lower);
    int b = (rand() % (upper - lower + 1) + lower);
    int c = (rand() % (upper - lower + 1) + lower);
    int valor_apostado;

    printf("Valor a apostar: R$");
    scanf("%d", &valor_apostado);

    printf("%d | %d | %d\n", a, b, c);

    if (a == b && b == c)
    {
        printf("Parabéns! Você conseguiu 3 números iguais e ganhou R$%d!\n", valor_apostado*100);
    } 
    else if (a == b || b == c || a == c)
    {
        printf("Parabéns! Você conseguiu 2 números iguais e ganhou R$%d!\n", valor_apostado*5);
    }
    else
    {
        printf("Você perdeu o jogo! Mais sorte na próxima vez!\n");
    }
    
}