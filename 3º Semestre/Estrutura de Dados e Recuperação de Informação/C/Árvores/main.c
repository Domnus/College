#include <stdio.h>
#include <stdlib.h>

struct NODE {
    struct NODE *left;
    int data;
    struct NODE *right;
};

typedef struct NODE TREE;

void insert(TREE **R, int n) {
    if (*R == NULL) {
        (*R) = (TREE *) malloc(1 * sizeof(TREE));
        (*R) -> data = n;
        (*R) -> left = NULL;
        (*R) -> right = NULL;
    } else if (n < (*R) -> data) {
        insert(&(*R) -> left, n);
    } else {
        insert(&(*R) -> right, n);
    }
}

void preOrder(TREE *R) {
    if (R != NULL) {
        printf("%d ", R -> data);
        preOrder(R -> left);
        preOrder(R -> right);
    }
}

void inOrder(TREE *R) {
    if (R != NULL) {
        inOrder(R -> left);
        printf("%d ", R -> data);
        inOrder(R -> right);
    }
}

void posOrder(TREE *R) {
    if (R != NULL) {
        posOrder(R -> left);
        posOrder(R -> right);
        printf("%d ", R -> data);
    }
}

void *search(TREE *R, int v) {
    if (R == NULL) {
        return NULL;
    } else if (R -> data == v) {
        return R;
    } else if (R -> data > v) {
        return search(R -> left, v);
    } else {
        return search(R -> right, v);
    }
}

void descendentes(TREE *R, int v) {
    if (R != NULL) {
        if (R -> data == v) {
            if (R -> left != NULL) {
                inOrder(R -> left);
            }
             if (R -> right != NULL) {
                inOrder(R -> right);
            }
        }
        descendentes(R -> left, v);
        descendentes(R -> right, v);
    }
}

void descendentesDiretos(TREE *R, int v) {
    if (R != NULL) {
        if (R -> data == v) {
            if (R -> left != NULL) {
                printf("%d ", R -> left -> data);
            }
             if (R -> right != NULL) {
                printf("%d ", R -> right -> data);
            }
        }
    }
}

TREE *searchPai(TREE *R, TREE *ret) {
    if (R -> left == ret || R -> right == ret) 
        return R;
    else if (R -> data > ret -> data) 
        return searchPai(R -> left, ret);
    else 
        return searchPai(R -> right, ret);
}

int main() {
    TREE *Root, *ret, *pai;
    int op, val;

    Root = NULL; 

    do {
        system("clear");

        puts("1 - Inserir na árvore");
        puts("2 - Percursos");
        puts("3 - Buscar um nó");
        puts("4 - Buscar Pai de um nó");
        puts("0 - Sair do programa");

        printf("\nDigite a opção: ");
        scanf("%d", &op);
        getchar();

        switch (op) {
            case 1:
                printf("\nDigite o valor a inserir: ");
                scanf("%d", &val);
                insert(&Root, val);
                break;
            
            case 2:
                printf("\nPre-Order:\n");
                preOrder(Root);

                printf("\nIn-Order:");
                inOrder(Root);

                printf("\nPos-Order:\n");
                posOrder(Root);

                getchar();
                break;
            
            case 3:
                printf("\nDigite o valor a procurar: ");
                scanf("%d", &val);

                ret = search(Root, val);

                if (ret == NULL) {
                    printf("\nValor não existe na árvore!\n");
                } else {
                    printf("\nValor existe na árvore: %d\n", ret -> data);
                }

                getchar();
                break;
            
            case 4:
                printf("\nDigite o nó a procurar:");
                scanf("%d", &val);

                ret = search(Root, val);

                if (ret == NULL) {
                    printf("\nValor não existe na árvore! Logo, não tem pai!\n");
                } else {
                    if (ret != Root){
                        pai = searchPai(Root, ret);
                        printf("\nO pai do %d é igual a %d\n", pai -> data, ret -> data);
                    }
                }
        }
    } while (op != 0);

    return 0;
}