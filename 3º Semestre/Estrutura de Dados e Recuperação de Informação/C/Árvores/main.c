#include <stdio.h>
#include <stdlib.h>

struct no_arvore {
    struct no_arvore *esq;
    int info;
    struct no_arvore *dir;
};

typedef struct no_arvore ARVORE;

ARVORE *CAPB (int N) {
    ARVORE *r;

    if (N == 0)
        r = NULL;
    else {
        r = (ARVORE *) calloc(1, sizeof(ARVORE));
        printf("\nDigite um valor --> ");
        scanf("%d", &r->info);

        r->esq = CAPB(N/2);
        r->dir = CAPB(N - N/2 -1);
    }
    return r;
}

void inOrder(ARVORE *r) {
    if (r != NULL) {
        inOrder(r->esq);
        printf(" %i ", r->info);
        inOrder(r->dir);
    }
}

void preOrder(ARVORE *r) {
    if (r != NULL) {
        printf(" %i ", r->info);
        preOrder(r->esq);
        preOrder(r->dir);
    }
}

void posOrder(ARVORE *r) {
    if (r != NULL) {
        posOrder(r->esq);
        posOrder(r->dir);
        printf(" %i ", r->info);
    }
}

void insere(ARVORE **R, int n) {
    if (*R == NULL) {
        (*R) = (ARVORE *) calloc(1, sizeof(ARVORE));
        (*R) -> info = n;
        (*R) -> esq = NULL;
        (*R) -> dir = NULL;
    } else if (n < (*R) -> info)  {
        insere(&(*R) -> esq, n);
    } else {
        insere(&(*R) -> dir, n);
    }
}

ARVORE *busca(ARVORE *R, int v) {
    if (R == NULL) {
        return NULL;
    } else if (R -> info == v) {
        return R;
    } else if (R -> info > v) {
        return busca(R -> esq, v);
    } else {
        return busca(R -> dir, v);
    }
}


int main() {
    ARVORE *Raiz;

    int N;

    printf("Digite a quantidade de nós da árvores -> ");
    scanf("%d", &N);

    Raiz = CAPB(N);

    printf("\npreOrder:\n");
    preOrder(Raiz);
    printf("\ninOrder:\n");
    inOrder(Raiz);
    printf("\nposOrder:\n");
    posOrder(Raiz);

    return 0;
}