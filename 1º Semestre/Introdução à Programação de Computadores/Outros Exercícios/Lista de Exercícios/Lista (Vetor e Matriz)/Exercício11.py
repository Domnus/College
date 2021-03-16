arr = []
multiplos = []

print('Digite 10 números: ')

for i in range(10):
    arr.append(int(input('-> ')))

print(f'Vetor: \n{arr}')

num = int(input('Informe o número desejado: '))

for i in arr:
    if i % num == 0:
        multiplos.append(i)

print(f'Há {len(multiplos)} múltiplos de {num}. São eles:\n{multiplos}')

