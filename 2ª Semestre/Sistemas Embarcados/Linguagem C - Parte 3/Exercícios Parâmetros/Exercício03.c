#include <stdio.h>

int antecessorSucessor(int num, int *sucessor, int *antecessor)
{
    *antecessor = num - 1;
    *sucessor = num + 1;
}

int main()
{
    int n, sucessor, antecessor;
    int list[2];
    printf("Digite um número: ");
    scanf("%d", &n);

    antecessorSucessor(n, &sucessor, &antecessor);
    printf("Antecessor: %d\nSucessor: %d\n", antecessor, sucessor);
}