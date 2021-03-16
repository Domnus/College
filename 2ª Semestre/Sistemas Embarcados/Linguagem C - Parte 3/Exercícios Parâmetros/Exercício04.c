#include <stdio.h>
#include <stdbool.h>

int elemInList(int list[10], int n)
{
    bool valid = false;
    for (int i = 0; i < 10; i++)
    {
        if (list[i] == n)
        {
            return i;
            valid = true;
            break;
        }
    }
    if (! valid)
    {
        return -1;
    }
}

int main()
{
    int list[10], pos, num;

    printf("Informe os elementos da lista: \n");
    for (int i = 0; i < 10; i++)
    {
        printf("-> ");
        scanf("%d", &list[i]);
    }

    printf("Informe o caractere: ");
    scanf("%d", &num);

    pos = elemInList(list, num);

    printf("%d está localizado no index %d.\n", num, pos);
}