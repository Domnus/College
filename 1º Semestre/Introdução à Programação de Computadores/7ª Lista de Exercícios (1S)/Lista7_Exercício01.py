from random import randint

arr = [0] * 2
soma = 0

for i in range(2):
    arr[i] = [0] * 3
    for j in range(3):
        arr[i][j] = randint(0, 9)

print('=' * 9)
print('Matriz:')
for i in range(2):
    for j in range(3):
        print(f'[{arr[i][j]}]', end= '')
    print()
print('=' * 9)

for i in range(2):
    for j in range(3):
        soma += arr[i][j]

print(f'A soma de todos os elementos da matriz será {soma}')
