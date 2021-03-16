n = int(input('Digite um número: '))
i = 1
somaImpares = 0

while somaImpares < n:
    somaImpares += i
    i += 2
    print(somaImpares)
    print(i)
if n == somaImpares:
    print('É um quadrado perfeito.')
else:
    print('Não é um quadrado perfeito.')



