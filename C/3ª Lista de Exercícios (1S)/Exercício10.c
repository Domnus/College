#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    srand(time(0));

    int lower = 1, upper = 36, count = 1;
    int num = (rand() % (upper - lower + 1) + lower);
    int guess;
    float valor_aposta;

    printf("%d\n", num);
    printf("Valor da Aposta: R$");
    scanf("%f", &valor_aposta);

    printf("Número a ser apostado (1 a 36): R$");
    scanf("%d", &guess);

    if (guess == num)
    {
        printf("Parabéns! Você acertou o número e ganhou R$%d.\n", guess*5);
    }
    else if ((guess / 12) == (num / 12))
    {
        printf("Parabéns! Você acertou a dúzia e ganhou R$%d.\n", guess*3);
    }
    else if ((guess % 2) == (num % 2))
    {
        printf("Parabéns! Você acertou a paridade e ganhou R$%d.\n", guess*2);
    }
    else
    {
        printf("Você não acertou nada! Mais sorte da próxima vez!\n");
    }


}
