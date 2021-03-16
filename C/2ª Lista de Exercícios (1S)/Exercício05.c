#include <stdio.h>

int main()
{

    float ang1, ang2, ang3;

    printf("Informe os ângulos do triângulo: \n");

    printf("1º ângulo: ");
    scanf("%f", &ang1);

    printf("2º ângulo: ");
    scanf("%f", &ang2);

    printf("3º ângulo: ");
    scanf("%f", &ang3);

    if (ang1 + ang2 + ang3 != 180){
        printf("Não é um triângulo!\n");
    }
    else if (ang1 > 90 && ang2 > 90 && ang3 > 90){
        printf("Acutângulo\n");
    }
    else if (ang1 == 90 || ang2 == 90 || ang3 == 90){
        printf("Triângulo Retângulo");
    }
    else if (ang1 > 90 || ang2 > 90 || ang3 > 90){
        printf("Obtusângulo");
    }
}
