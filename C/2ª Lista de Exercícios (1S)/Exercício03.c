#include <stdio.h>

int main()
{

    int op;
    float area, base, altura;

    printf("OP 1 = Área do retângulo\nOP 2 = Área do triângulo\n");
    
    printf("OP = ");
    scanf("%d", &op);

    printf("Base = ");
    scanf("%f", &base);

    printf("Altura = ");
    scanf("%f", &altura);

    if (op == 1){
        area = base * altura;
        printf("A área do retângulo é igual a %f.\n", area);
    }
    else if (op == 2){
        area = (base * altura) / 2;
        printf("A área do triângulo é igual a %f\n", area);
    }
    
}