#include <stdio.h>
#include <stdlib.h>

#define TAM 10

void criaFila(int *Head, int *Tail) {
    *Head = 0;
    *Tail = 0;
}

int insFila(int *F, int *Head, int *Tail, int v) {
    if ((*Tail + 1) % TAM == *Head) {
        return 0;
    } else {
        *Tail = (*Tail + 1) % TAM;
        F[*Tail] = v;
        return 1;
    }
}

int remFila(int *F, int *Head, int *Tail, int *v) {
    if (*Head == *Tail) {
        return 0;
    } else {
        *Head = (*Head + 1) % TAM;
        *v = F[*Head];
        return 1;
    }
}

void imprime(int *F, int Head, int Tail) {
    int i = Head;

    do {
        i = (i + 1);
        printf("[ %d ] ", F[i]);
    } while (i != Tail);
}

int main() {
    int F[TAM], Head, Tail;

    int val, op;

    criaFila(&Head, &Tail);

    do {
        system("clear");
        puts("1 - Inserir na Fila");
        puts("2 - Remover da Fila");
        puts("3 - Imprimir a Fila");
        
        puts("0 - Sair do programa");

        printf("\nDigite a opção -> ");
        scanf("%d", &op);
        getchar();

        switch(op) {
            case 1: 
                printf("\nDigite o valor a inserir: ");
                scanf("%d", &val);

                if (insFila(F, &Head, &Tail, val)) 
                    printf("\nInserção com sucesso!\n");
                else 
                    printf("\nFila Cheia!\n");

                getchar();
                getchar();
                break;
            
            case 2:
                if (remFila(F, &Head, &Tail, &val))
                    printf("\nValor removido = %d\n", val);
                else 
                    printf("\nFila Vazia!\n");

                getchar();
                break;

            case 3:
                if (Head == Tail)
                    printf("\nFila Vazia!\n");
                else {
                    printf("\nFila:\n");
                    imprime(F, Head, Tail);
                }

                getchar();
                break;
        }
    } while (op != 0);
}