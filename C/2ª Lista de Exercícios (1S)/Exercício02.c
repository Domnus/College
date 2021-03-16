#include <stdio.h>
#include <stdlib.h> 

int main()
{
    int numPlaca;
    int fimPlaca;

    printf("Digite a parte numérica da placa [XXXX]: ");
    scanf("%d", &numPlaca);

    fimPlaca = ((numPlaca % 1000) % 100) % 10;
    
    if (numPlaca > 9999 || numPlaca < 1000){
        printf("Número inválido. Digite um número com 4 algarismos.\n");
    }
    else if (fimPlaca == 1 || fimPlaca == 2){
        printf("Dia do Rodízio: Segunda-Feira\n");
    }
    else if (fimPlaca == 3 || fimPlaca == 4){
        printf("Dia do Rodízio: Terça-Feira\n");
    }
    else if (fimPlaca == 5 || fimPlaca == 6){
        printf("Dia do Rodízio: Quarta-Feira\n");
    }
    else if (fimPlaca == 7 || fimPlaca == 8){
        printf("Dia do Rodízio: Quinta-Feira\n");
    }
    else if (fimPlaca == 9 || fimPlaca == 0){
        printf("Dia do Rodízio: Sexta-Feira\n");
    }
}