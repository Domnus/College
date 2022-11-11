#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>

typedef struct {
	char nome[50];
	int preco;
} Item;

int somaCarrinho(Item *carrinho, int tamanho) {
	int i, soma = 0;
	for (i = 0; i < tamanho; i++) {
		soma += carrinho[i].preco;
	}
	return soma;
}

void* executaCarrinho(void *arg) {
	int numero = *(int*)arg;
    
	Item carrinho[3];
	carrinho[0] = (Item){"Iphone", 499};
    carrinho[1] = (Item){"Kindle", 179};
    carrinho[2] = (Item){"Macbook Pro", 1199};
	
    int total = somaCarrinho(carrinho, sizeof(carrinho)/sizeof(Item));
	
    printf("[%d] O total do carrinho é %d\n", numero, total);
	return NULL;
}

int main(void) {
    clock_t begin = clock(); // Inicia a contagem de tempo
    pthread_t thread_id;

	int num1 = 1;
    pthread_create(&thread_id, NULL, executaCarrinho, &num1);
	int num2 = 2;
    pthread_create(&thread_id, NULL, executaCarrinho, &num2);
	int num3 = 3;
    pthread_create(&thread_id, NULL, executaCarrinho, &num3);
	int num4 = 4;
    pthread_create(&thread_id, NULL, executaCarrinho, &num4);
	int num5 = 5;
    pthread_create(&thread_id, NULL, executaCarrinho, &num5);

	pthread_join(thread_id, NULL);

    clock_t end = clock(); // Finaliza a contagem de tempo
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC; // Calcula o tempo gasto

	printf("Tempo de execução: %0.2f ms", time_spent * 1000);
	return 0;
}