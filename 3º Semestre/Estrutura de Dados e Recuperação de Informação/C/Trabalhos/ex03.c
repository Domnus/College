#include <stdio.h>
#include <stdlib.h>

struct dados
{
    struct dados *esq;
    int info;
    struct dados *dir;
};

typedef struct dados NO;

void Cria_LDE(NO **Inicio, NO **Fim)
{
    *Inicio = NULL;
    *Fim = NULL;
}

typedef struct dados NO;

void Ins_Inicio(NO **Inicio, NO **Fim, int val)
{
    NO *p = (NO *)calloc(1, sizeof(NO));

    p->info = val;
    p->esq = NULL;
    p->dir = *Inicio;

    if (*Inicio == NULL)
    {
        *Fim = p;
    }
    else
    {
        (*Inicio)->esq = p;
    }

    *Inicio = p;
}

void Ins_Fim(NO **Inicio, NO **Fim, int val)
{
    NO *p = (NO *)calloc(1, sizeof(NO));

    p->info = val;
    p->dir = NULL;
    p->esq = *Fim;

    if (*Inicio == NULL)
    {
        *Inicio = p;
    }
    else
    {
        (*Fim)->dir = p;
    }

    *Fim = p;
}

void Imprime(NO *Inicio)
{
    NO *p = Inicio;

    printf("\nNULL");

    while (p != NULL)
    {
        printf("<-- %d -->", p->info);
        p = p->dir;
    }

    printf("NULL\n\n");
}

int contaLista(NO *Inicio)
{
    NO *p = (NO *) calloc(1, sizeof(NO)); 
    p = Inicio;
    int contador = 0;

    while (p != NULL)
    {
        contador++;
        p = p -> dir;
    }

    return contador;
}

void restaUm(NO **Inicio, NO **Fim, int valor)
{
    system("clear");
    getchar();
    NO *p = *Inicio, *q;

    while (contaLista(*Inicio) > 1) {
        int contador = 1; 

        while (contador != valor) {
            if (p == *Fim) {
                p = *Inicio;
            } else {
                p = p -> dir;
            }
            contador++;
        }

         if (p == *Inicio) {
            *Inicio = p -> dir;
        }

        q = p;
        
        if (p -> esq != NULL){
            p -> esq -> dir = p -> dir;
        }

        if (p -> dir != NULL) {
            p -> dir -> esq = p -> esq;
        }

        if (p == *Fim) {
            *Fim = (*Fim) -> esq;
            p = *Inicio;
        } else {
            p = p -> dir;
        }
       
        free(q);

        Imprime(*Inicio);
        getchar();
    }

    printf("Resta Um -> %d", (*Inicio) -> info);
    getchar();
}

int main()
{
    NO *Inicio, *Fim;
    int val, op;

    Cria_LDE(&Inicio, &Fim);

    do
    {
        system("clear");
        puts("1 - Inserir no Inicio");
        puts("2 - Inserir no Fim");
        puts("3 - Imprimir na lista");
        puts("4 - Resta 1");
        puts("0 - Sair do programa");

        printf("\nDigite a opção -> ");
        scanf("%d", &op);
        getchar();

        switch (op)
        {
        case 1:
            printf("Digite o valor a inserir -> ");
            scanf("%d", &val);
            Ins_Inicio(&Inicio, &Fim, val);
            break;

        case 2:
            printf("Digite o valor a inserir -> ");
            scanf("%d", &val);
            Ins_Fim(&Inicio, &Fim, val);
            break;

        case 3:
            if (Inicio == NULL)
            {
                printf("\nLista Vazia!\n");
            }
            else
            {
                Imprime(Inicio);
            }

            getchar();
            break;

        case 4:
            printf("Digite um número: ");
            scanf("%d", &val);

            restaUm(&Inicio, &Fim, val);
            Imprime(Inicio);

            break;
        }

    } while (op != 0);

    return 0;
}