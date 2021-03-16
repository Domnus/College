#include <stdio.h>
#include <stdlib.h>

struct dados{
    char nome[30];
    float n1;
    float n2;
};

typedef struct dados No;

void imprime(No *l, int f) {
    for (int i = 0; i < f; i++) {
        printf("\nNome....: %s", l[i].nome);
        printf("\nNota 1..: %.2f", l[i].n1);
        printf("\nNota 2..: %.2f\n", l[i].n2);
    }
}

int insFim(No *L, int *f, No a) {
    if (*f < 10) {
        L[(*f)] = a;
        (*f)++;
        return 1;
    }
    else {
        return 0;
    }
}

int main() {

    No lista[10];

    int fim = 0;
    int op;

    No aluno;

    do {
        puts("1 - Inserir no Fim da Lista");
        puts("2 - Imprimir a Lista");
        puts("3 - Inserir na posição K");
        puts("4 - Remover na posição K");
        puts("5 - ");
        puts("0 - Sair do programa");

        printf("Digite a opção: ");
        scanf("%d", &op);

        system("clear");
        switch (op) {
            case 1:
                printf("Digite o nome do aluno: ");
                fflush(stdin);
                scanf("%s", aluno.nome);
                printf("Digite a nota 1: ");
                scanf("%f", &aluno.n2);
                printf("Digite a nota 2: ");
                scanf("%f", &aluno.n2);

                if (insFim(lista, &fim, aluno)){
                    printf("Inserção realizada com sucesso!\n");
                }
                else {
                    printf("Lista cheia!");
                }
                break;
            case 2:
                if (fim == 0) {
                    printf("Lista vazia!\n");
                }
                else {
                    printf("Lista:\n");
                    imprime(lista, fim);
                }
                break;
        }
        int c = getchar();
    } while (op != 0);

   return 0;
 }