#include <stdio.h>
#include <stdbool.h>

int main()
{
    int n, x, i, j;
    int valid;
    int nulo = 0;

    printf("Informe o tamanho da matriz: ");
    scanf("%d", &n);

    int arr[n][n]; 
    
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("Valor de [%d][%d]: ", i, j);
            scanf("%d", &arr[i][j]);
        }
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf(" [%d]", arr[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < n; i++)
    {
        valid = 0;
        for (j = 0; j < n; j++)
        {
            if (arr[j][i] == 0)
            {
                valid++;
            }
        }
        if (valid == n)
        {
            nulo++;
        }
    }

    if (nulo == 0)
    {
        printf("Não há colunas nulas na matriz.\n");
    }
    else if (nulo == n)
    {
        printf("A matriz é nula.\n");
    }
    else
    {
        printf("Há %d colunas nulas na matriz.\n", nulo);
    }
    
}