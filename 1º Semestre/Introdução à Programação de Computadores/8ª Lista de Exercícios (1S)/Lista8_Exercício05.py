from random import randint

arr = [0] * 5
diagonal_principal = []
diagonal_secundaria = []

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(1, 50)

print('=' * 20)
print('Matriz:')
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()


for i in range(5):
    for j in range(5):
        if i == j:
            diagonal_principal.append(arr[i][j])
        if j == 4 - 1:
            diagonal_secundaria.append(arr[i][4-i])

for i in range(5):
    for j in range(5):
        if i == j:
            arr[i][j] = diagonal_secundaria[i]
        elif j == 4 - i:
            arr[i][4-i] = diagonal_principal[i]

print('=' * 20)
print('Resultado:')
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 20)

