#include <stdio.h>
#include <string.h>

int main() {
    char times[5][30];
    int n;
    int nVitorias[5];
    int tempoVitorias[5];
    char nome[30];
    int tempo;

    printf("Digite o nome dos times: ");
    for (int i = 0; i< 5; i++) {
        scanf("%s", times[i]);
    }

    printf("Digite o número de partidas: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%s %d", nome, &tempo);
        int pos = -1;
        for (int j = 0; j < 5; j++) {
            if (strcmp(nome, times[j]) == 0) {
                pos = j;
            }
        }

        if (pos >= 0) {
            nVitorias[pos] = nVitorias[pos] + 1;
            tempoVitorias[pos] = tempoVitorias[pos] + tempo;
        }
    }

    for (int i = 0; i < 5; i++) {
        printf("%s: %f", times[i], (float) tempoVitorias[i]/nVitorias[i]);
    }

    return 0;
}