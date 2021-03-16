#include <stdio.h>

int main()
{
    int n1, n2, n3, n;

    printf("1º número: ");
    scanf("%d", &n1);

    printf("2º número: ");
    scanf("%d", &n2);

    printf("3º número: ");
    scanf("%d", &n3);

    if (n1 > n2){
        n = n1;
        n1 = n2;
        n2 = n;
    }
    if (n2 > n3){
        n = n2;
        n2 = n3;
        n3 = n;
    }
    if (n1 > n2){
        n = n1;
        n1 = n2;
        n2 = n;
    }

    printf("%d | %d | %d\n", n1, n2, n3); 

    return 0;
}