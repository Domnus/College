#include <stdio.h>
#include <stdlib.h>

#define tam 10

typedef struct 
{
	int info[tam];
	int topo;
} PILHA;

void Inicializa(PILHA *p) {
	p -> topo = -1;
}

int cheia(PILHA *p) {
	return (p->topo == tam-1);
}

int vazia(PILHA *p) {
	return (p-> topo == -1);
}

int push(PILHA *p, int v) {
	if (cheia(p)) 
		return 0;

	p -> info[++p -> topo] = v;
	return 1;
}

int pop(PILHA *p, int *v) {
	if (vazia(p)) 
		return 0;
	
	*v = p -> info[p->topo--];
	return 1;
}

void imprime(PILHA p) {
	for (int i = p.topo; i >= 0; i--) 
		printf(" [ %d ]\n", p.info[i]);
}

int transformaBinario(PILHA *p, int val) {
	int valorBinario = 0;

	while (val > 0) {
		push(p, val % 2);

		val /= 2;
	}
	
	while (!vazia(p)) {
		pop(p, &val);
		valorBinario = valorBinario * 10 + val;
	}

	return valorBinario;

}

int main() {
	PILHA S;
	int op, val;

	Inicializa(&S);

	do {
		system("clear");
		puts("1 - Inserir na Pilha");
		puts("2 - Remover da Pilha");
		puts("3 - Imprimir a Pilha");
		puts("4 - Transformar número em binário");

		puts("0 - Sair do programa");
		printf("Digite a opção: ");
		scanf("%d", &op);
		getchar();

		switch(op) {
			case 1:
				printf("Digite o valor a inserir: ");
				scanf("%d", &val);

				if (push(&S, val))
					printf("\nInserção com sucesso!\n");
				else
					printf("\nPilha cheia!\n");

				getchar();
				break;

			case 2:
				if (pop(&S, &val))	
					printf("\nValor removido: %d\n", val);
				else 
					printf("\nPilha vazia!\n");
				
				getchar();
				break;

			case 3:
				if (vazia(&S))
					printf("\nPilha vazia!\n");
				else {
					printf("\n PILHA: \n");
					imprime(S);
				}

				getchar();
				break;

			case 4: 
				printf("Digite um número para transformar em binário: ");
				scanf("%d", &val);
				int nb = transformaBinario(&S, val);
				printf("Número em binário: %d\n", nb)	;

				getchar();
				getchar();
				break;
		}
	} while (op != 0);

	return 0;
}
