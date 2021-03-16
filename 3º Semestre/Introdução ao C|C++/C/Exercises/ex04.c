#include <stdio.h>
#include <stdlib.h>

int main() {
	int idade, p, *pessoas;
	
	scanf("%d", &p);

	pessoas = (int*)  malloc(p*sizeof(int));

	for (int i = 0; i < p; i++) {
		scanf("%d", pessoas+i);
	}

	for (int i = p-1; i >= 0; i--) {
		printf("%d", *(pessoas+i));
	}

	return 0;
}
