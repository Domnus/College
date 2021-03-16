#include <stdio.h>

int main()
{
    int n1, n2;
    printf("Digite o primeiro número: ");
    scanf("%d", &n1);
    printf("Digite o outro número: ");
    scanf("%d", &n2);

    if (n1 > n2) {
        printf("%d é maior que %d. A diferença entre eles é de %d.\n", n1, n2, n1 - n2);
    }
    else {
        printf("%d é maior que %d. A diferença entre eles é de %d.\n", n2, n1, n2 - n1);
    }
}