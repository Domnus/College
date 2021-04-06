#include <stdio.h>
#include <stdlib.h>

struct dados
{
    int info;
    struct dados *prox;

};

typedef struct dados NO;

void Cria_LSE(NO **Inicio)
{
    *Inicio = NULL;
}

void Ins_Inicio(NO **Inicio, int v)
{
    NO *p = (NO *)calloc(1, sizeof(NO));

    p->info = v;
    p->prox = *Inicio;
    *Inicio = p;
}

void Ins_Fim(NO **Inicio, int v)
{

    NO *p = (NO *)calloc(1,sizeof(NO));
    NO *q;

    p->info = v;
    p->prox = NULL;

    if (*Inicio == NULL)
        *Inicio = p;
    else
    {
        q = *Inicio;
        while (q->prox != NULL)
            q = q->prox;

        q->prox = p;
    }

}

int Rem_Inicio(NO **Inicio, int *v)
{
    NO *p = *Inicio;

    if (*Inicio == NULL)
        return 0;
    else
    {
        *Inicio = p->prox;
        *v = p->info;
        free(p);
        return 1;
    }

}

int Rem_Fim(NO **Inicio, int *v)
{
    NO *p = *Inicio;
    NO *q;

    if (*Inicio == NULL)
        return 0;
    else
    {
        // Verificar se só existe um nó

        if (p->prox == NULL)
            *Inicio = NULL;  // alterando o Inicio
        else
        {
            // prreciso colocar o p no ultimo nó e o q
            // no penultimo

            while (p->prox != NULL)
            {
                q = p;
                p = p->prox;
            }

            q->prox = NULL;
        }
        *v = p->info;
        free(p);
        return 1;
    }
}


NO * Consulta(NO *Inicio, int v)
{
    NO *p = Inicio;

    while ((p!=NULL) && (p->info!=v))
        p = p->prox;

    return p;
}

void Rem_Meio(NO *Inicio, NO *r)
{
    NO *p = Inicio;

    // posicionar p no nó que aponta para r (anterior)

    while (p->prox != r)
        p = p->prox;


    p->prox = r->prox;

    free(r);
}


void Ins_Depois(NO *r, int v)
{
    NO *p = (NO *)calloc(1, sizeof(NO));

    p->info = v;

    p->prox = r->prox;

    r->prox = p;
}


void Ins_Antes(NO *Inicio, NO *r, int v)
{
    NO *p = (NO *) calloc(1, sizeof(NO));
    NO *q = Inicio;

    p->info = v;
    p->prox = r;

    while (q->prox != r)
        q = q->prox;

    q->prox = p;
}

void Imprime(NO *Inicio)
{
    NO *p = Inicio;

    while (p!=NULL)
    {
        printf("%d-->", p->info);
        p = p->prox;

    }
    printf("NULL\n");
}

int main()
{
    NO *Inicio;
    // ponteiro que ira indicar um nó da lista caso ele exista
    NO *r;
    int val, op;

    // criando a lista vazia
    Cria_LSE(&Inicio);

    do {
        system("clear");
        puts("1 - Inserir no Inicio");
        puts("2 - Imprimir a Lista");
        puts("3 - Inserir no Fim");
        puts("4 - Remover no Inicio");
        puts("5 - Remover no Fim ");
        puts("6 - Consultar um Valor");
        puts("7 - Remover um Valor");
        puts("8 - Inserir depois de Valor");
        puts("9 - Inserir antes de valor");

        puts("10 - Inserir de forma ordenada");


        puts("0 - Sair do programa");

        printf("\nDigite a opcao:");
        scanf("%d", &op);

        switch(op)
        {
            case 1: printf("Digite o valor a inserir:");
                scanf("%d", &val);
                Ins_Inicio(&Inicio, val);
                break;

            case 2: if (Inicio!=NULL)
                {
                    printf("\nInicio:\n");
                    Imprime(Inicio);
                }
                else
                    printf("\nLista Vazia!\n");
                system("pause");
                break;

            case 3: printf("Digite o valor a inserir:");
                scanf("%d", &val);
                Ins_Fim(&Inicio, val);
                break;

            case 4: if (Rem_Inicio(&Inicio, &val))
                    printf("\nFoi removido: %d\n", val);
                else
                    printf("\nLista Vazia!\n");

                system("pause");
                break;

            case 5: if (Rem_Fim(&Inicio, &val))
                    printf("\nFoi removido: %d\n", val);
                else
                    printf("\nLista Vazia!\n");

                system("pause");
                break;

            case 6: printf("\nDigite o valor a procurar: ");
                scanf("%d", &val);

                r = Consulta(Inicio, val);

                if (r==NULL)
                    printf("\nO valor %d nao existe na lista!\n", val);
                else
                    printf("\nValor encontrado: %d\n", r->info);

                system("pause");
                break;


            case 7: printf("\nDigite o valor a remover: ");
                scanf("%d", &val);

                r = Consulta(Inicio, val);

                if (r==NULL)
                    printf("\nO valor %d nao existe na lista!\n", val);
                else
                {
                    if (r == Inicio)
                        Rem_Inicio(&Inicio, &val);
                    else
                    if (r->prox == NULL)
                        Rem_Fim(&Inicio, &val);
                    else
                        Rem_Meio(Inicio, r);

                    printf("\nRemocao com sucesso!\n");

                }
                system("pause");
                break;

            case 8: printf("\nDigite o valor a procurar: ");
                scanf("%d", &val);

                r = Consulta(Inicio, val);

                if (r==NULL)
                    printf("\nO valor %d nao existe na lista!\n", val);
                else
                {
                    printf("\nDigite o valor a inserir: ");
                    scanf("%d", &val);

                    if (r->prox==NULL)  // r é o ultimo
                        Ins_Fim(&Inicio, val);
                    else
                        Ins_Depois(r, val);

                    printf("\nInsercao com Sucesso!\n");
                }
                system("pause");
                break;

            case 9: printf("\nDigite o valor a procurar: ");
                scanf("%d", &val);

                r = Consulta(Inicio, val);

                if (r==NULL)
                    printf("\nO valor %d nao existe na lista!\n", val);
                else
                {
                    printf("\nDigite o valor a inserir: ");
                    scanf("%d", &val);

                    if (r==Inicio)
                        Ins_Inicio(&Inicio, val);
                    else
                        Ins_Antes(Inicio, r, val);

                    printf("\nInsercao com Sucesso!\n");
                }
                system("pause");
                break;
        } // fim do switch

    } while (op!=0);  // do

    return 0;
} // main
