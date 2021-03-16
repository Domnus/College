#include <stdio.h>

struct aluno {
	char nome[30];
	int nota;
};

typedef struct aluno ALUNO;

int main() {
	
	int a, me1 = 11, me2 = 11, p1, p2; 
	printf("Número de alunos: ");
	scanf("%d", &a);

	ALUNO alunos[a];

	for (int i = 0; i < a; i++) {
		printf("%dº aluno -> ", i+1);
		scanf("%s", alunos[i].nome);
		printf("%dª nota -> ", i+1);
		scanf("%d", &alunos[i].nota);
	}

	for (int i = 0; i < a; i++) {
		if (alunos[i].nota < me1) {
			me1 = alunos[i].nota;
			p1 = i;
		}
	}
	
	for (int i = 0; i < a; i++) {
		if (alunos[i].nota < me2 && i != p1) {
			me2 = alunos[i].nota;
			p2 = i;
		}
	}

	printf("Alunos com as 2 menores notas: \n");
	printf("-> Aluno: %s. Nota: %d\n", alunos[p1].nome, alunos[p1].nota);
	printf("-> Aluno: %s. Nota: %d", alunos[p2].nome, alunos[p2].nota);

	return 0;
}
