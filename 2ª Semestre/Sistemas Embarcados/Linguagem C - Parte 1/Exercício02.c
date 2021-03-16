#include <stdio.h>

int main()
{
  float preco;

  printf("Preço da compra: R$");
  scanf("%f", &preco);

  if (preco >= 500.0)
  {
    printf("O valor da compra com desconto é de R$%.2f.\n", preco * 0.75);
  }
  else if (preco >= 200.0)
  {
    printf("O valor da compra com desconto é de R$%.2f.\n", preco * 0.80);
  }
  else if (preco < 200.0)
  {
    printf("O valor da compra com desconto é de R$%.2f.\n", preco * 0.85);
  }
}
