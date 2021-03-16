#include <stdio.h>

void main()
{
		int a[10], i, m = 0;

		printf("Digite os elementos do vetor: ");
		for (i = 0; i < 10; i++)
		{
			scanf("%d", &a[i]);
		}

		for (i = 0; i < 10;i++)
		{
			if (a[i] > m)
			{
				m = a[i];
			}
		}

		printf("O maior valor do vetor é: %d", m);
}
