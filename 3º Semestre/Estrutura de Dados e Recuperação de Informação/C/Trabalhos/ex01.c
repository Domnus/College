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

void imprime(NO *Inicio){
    NO *p = Inicio;

    while (p != NULL){
        printf("%d --> ", p->info);
        p = p -> prox;
    }
    printf("NULL\n");
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

int Rem_Fim(NO **Inicio, NO **Fim, int *v){
    NO *p;
    NO *q;

    if (*Inicio == NULL){
        return 0;
    } else {
        p = *Fim;
        *v = p -> info;

        if (p == *Inicio){
            *Inicio = NULL;
            *Fim == NULL;
        } else {
            q = *Inicio;

            while (q -> prox != *Fim){
                q = q -> prox;
            }

            q -> prox = NULL;
            *Fim = q;
        }

        free(p);
        return 1;
    }
}

NO * Consulta(NO *Inicio, int v){
    NO *p = Inicio;

    while (p != NULL && p -> info != v){
        p = p-> prox;
    }

    return p;
}

int moveInicio(NO **Inicio, NO **Fim, int v){
    NO *p = *Inicio;
    NO *r;

    if (Consulta(*Inicio, v)){
        while (p != NULL && p -> info != v){
            r = p;
            p = p -> prox;
        }
        r -> prox =  p -> prox; 
        p -> prox = (*Inicio) -> prox;
        *Inicio = p;

    } else {
        return 0;
    }

    return 1;
}

int main(){
    NO *Inicio, *Fim, *r;
    int val, op;

    cria_LSE(&Inicio, &Fim);

    do {

        puts("1 - Inserir no Início");
        puts("2 - Inserir no Fim");
        puts("3 - Imprimir a lista");
        puts("4 - Remover no Inicio");
        puts("5 - Remover no Fim");
        puts("6 - Consultar um valor");
        puts("7 - Mover para o Início");
        puts("8 - Mover para o Fim");
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
            
            case 5:
                if (Rem_Fim(&Inicio, &Fim, &val)){
                    printf("\nFoi removido: %d\n", val);
                } else {
                    printf("\nLista vazia!\n");
                }
                getchar();
                getchar();
                break;
            
            case 6:
            printf("\nDigite o valor a procurar: ");
            scanf("%d", &val);

            r = Consulta(Inicio, val);

            if (r == NULL){
                printf("\nValor não existe na lista!");
            } else {
                printf("\nValor encontrado: %d", r->info);
            }

            getchar();
            getchar();

            break;
        
            case 7:
                printf("Digite o valora para mudar para o Inicio da lista: ");
                scanf("%d", &val);

                if (moveInicio(&Inicio, &Fim, val)){
                    printf("Valor %d mudado para o começo da lista!", val);
                } else {
                    printf("Não foi possível mover o valor!");
                }

                getchar();
                getchar();

                break;

            case 8:
                printf("Digite o valora para mudar para o Inicio da lista: ");
                scanf("%d", &val);


                break;
        }

    } while (op != 0);


    return 0;
}