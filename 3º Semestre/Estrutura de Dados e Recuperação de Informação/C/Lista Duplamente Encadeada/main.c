#include <stdio.h>

struct dados
{
    int info;
    struct dados *prox;
};

typedef struct dados NO;

void cria_LSE(NO **Inicio, NO **Fim){
    *Inicio = NULL;
    *Fim = NULL;
}

void Ins_Inicio(NO **Inicio, NO **Fim, int v){
    NO *p = (NO *) calloc(1, sizeof(NO));

    p -> info = v;
    p -> prox = *Inicio;

    if (*Inicio == NULL){
        *Fim = p;
    }

    *Inicio = p;
}

void Ins_Fim(NO **Inicio, NO **Fim, int v){
    NO *p = (NO *) calloc(1, sizeof(NO));

    p -> info = v;
    p -> prox = NULL;

    if (*Inicio == NULL){
        *Inicio = p;
    } else {
        (*Fim) -> prox = p;
    }

    *Fim = p;
}

int Rem_Inicio(NO **Inicio, NO **Fim, int *v){
    NO *p;

    if (Inicio == NULL){
        return 0;
    } else {
        p = *Inicio;
        *v = p -> info;

        *Inicio = p -> prox;

        if (p -> prox == NULL){
            *Fim = NULL;
        
        free(p);
        return 1;
        }
    }
}

void imprime(NO *Inicio){
    NO *p = Inicio;

    while (p != NULL){
        printf("%d --> ", p->info);
        p = p -> prox;
    }
    printf("NULL\n");
}

int main(){
    NO *Inicio, *Fim;
    int val, op;

    cria_LSE(&Inicio, &Fim);

    do {

        system("clear");
        puts("1 - Inserir no Início");
        puts("2 - Inserir no Fim");
        puts("3 - Imprimir a lista");
        puts("4 - Remover no Inicio");
        puts("5 - Remover no Fim");
        puts("6 - Consultar um valor");
        puts("0 - Sair do programa");

        printf("\nDigite a opção: ");
        scanf("%d", &op);

        switch(op){
            case 1:
                printf("Digite o valor a inserir: ");
                scanf("%d", &val);
                Ins_Inicio(&Inicio, &Fim, val);
                break;

            case 2:
                printf("Digite o valor a inserir: ");
                scanf("%d", &val);
                Ins_Fim(&Inicio, &Fim, val);
                break;
            
            case 3:
                if (Inicio == NULL){
                    printf("\nLista vazia!\n");
                } else {
                    printf("\nLista:\n");
                    imprime(Inicio);
                }
                getchar();
                getchar();
                break;
            
            case 4:
                if (Rem_Inicio(&Inicio, &Fim, &val)){
                    printf("\nFoi removido: %d\n", val);
                } else {
                    printf("\nLista vazia!\n");
                }

                getchar();
                getchar();
                break;
        }

    } while (op != 0);


    return 0;
}