num = int(input('Digite o número desejado: '))
soma = 0
for i in range(1, num):
    if num % i == 0:
        soma += i

print(f'A soma dos divisores de {num} é {soma}')