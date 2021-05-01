#include <stdio.h>
#include <stdlib.h>

#define tam 10

typedef struct
{
    int info[tam];
    int topo;
} PILHA;

void begin(PILHA *p)
{
    p->topo = -1;
}

int full(PILHA *p)
{
    return (p->topo == tam - 1);
}

int empty(PILHA *p)
{
    return (p->topo == -1);
}

int push(PILHA *p, int v)
{
    if (full(p))
        return 0;

    p->info[++p->topo] = v;
    return 1;
}

int pop(PILHA *p, int v)
{
    return (p->info[p->topo--]);
}

void orderedPush(PILHA *p, PILHA *aux, int v)
{
    for (int i = p -> topo; i >= 0; i--) {
        int x = p -> info[i];
        if (x <= v) {
            push(aux, x);
            pop(p, x);
        }
    }

    push(p, v);

    for (int i = aux -> topo; i >= 0; i--) {
        push(p, aux -> info[i]);
        pop(aux, aux -> info[i]);
    }

}

void print(PILHA p)
{
    int i;
    for (i = p.topo; i >= 0; i--)
        printf(" [ %d ]\n", p.info[i]);
}

int main()
{
    PILHA pilha, aux;
    int op, val;

    begin(&pilha);
    begin(&aux);

    do
    {
        system("clear");
        puts("1 - Inserir na Pilha");
        puts("2 - Remover da Pilha");
        puts("3 - Imprimir a Pilha");
        puts("4 - Inserir ordenadamente na pilha");

        puts("0 - Finalizar");
        printf("\nDigite a opção: ");
        scanf("%d", &op);
        getchar();

        switch (op)
        {
        case 1:
            printf("\nDigite o valor a inserir: ");
            scanf("%d", &val);
            if (push(&pilha, val))
                printf("\nInserção com sucesso!\n");
            else
                printf("\nPilha Cheia!\n");

            getchar();
            getchar();
            break;

        case 2:
            if (empty(&pilha))
                printf("\nPilha Vazia!\n");
            else {
                pop(&pilha, val);
                printf("\nValor removido!\n");
            }

            getchar();
            break;

        case 3:
            if (empty(&pilha))
                printf("\nPilha Vazia!\n");
            else
            {
                printf("\n PILHA: \n");
                print(pilha);
            }
            getchar();
            break;

        case 4:
            if (full(&pilha))
                printf("Pilha cheia!\n");
            else {
                printf("Digite o valor a inserir: ");
                scanf("%d", &val);
                orderedPush(&pilha, &aux, val);
                printf("Pilha ordenada!");
            }

            getchar();
            getchar();
            break;
        }
    } while (op != 0);

    return 0;
}