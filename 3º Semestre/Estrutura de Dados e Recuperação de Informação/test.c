#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct dados {
	int info;
	struct dados *prox;
};

typedef struct dados NO;

void criaLSE(NO **Inicio){
	*Inicio = NULL;
}

void insInicio(NO **Inicio, int v){
	NO *p = (NO *)malloc(1 * sizeof(NO));

	p -> info = v;
	p -> prox = *Inicio;

	*Inicio = p;
}

void imprime(NO *Inicio){
	NO *p = Inicio;

	while (p != NULL){
		printf("%d-> ", p->info);
		p = p->prox;
	}

	printf("NULL\n");
}

void insFim(NO **Inicio, int v){
	NO *p = (NO *)malloc(1 * sizeof(NO));
	NO *q;

	p -> info = v;
	p -> prox = NULL;

	if (*Inicio == NULL){
		*Inicio = p;
	} else {
		q = *Inicio;
		while (q->prox != NULL){
			q = q -> prox;
		}
		q -> prox = p;
	}
}

int main(){
	NO *Inicio;
	int val, op;

	criaLSE(&Inicio);

	do {
		system("clear");
		puts("1 - Inserir no Inicio");
		puts("2 - Imprimir a Lista");
		puts("0 - Sair do programa");

		printf("\nDigite a opção: ");
		fflush(stdin);
		scanf("%d", &op);

		switch(op){
			case 1:
				printf("Digite o valor a inserir: ");
				scanf("%d", &val);
				insInicio(&Inicio, val);
				break;
			case 2:
				if (Inicio != NULL){
					printf("\nInicio:\n");
					imprime(Inicio);
				}
				getchar();
				break;

		}
	} while (op != 0);

	return 0;
}


