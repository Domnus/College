#include <stdio.h>

int main()
{
    int list1[10], list2[10], list3[10];
    int n;

    printf("Lista 1:\n");

    for (int i = 0; i < 10; i++)
    {
        printf("-> ");
        scanf("%d", &list1[i]);
    }

    printf("Lista 2:\n");

    for (int i = 0; i < 10; i++)
    {
        printf("-> ");
        scanf("%d", &list2[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        list3[i] = list1[i] + list2[i]; 
    }

    printf("Lista 3: ");
    for (int i = 0; i < 10; i++)
    {
        printf("[%d]", list3[i]);
    }

    printf("\n");
}
