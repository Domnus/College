from random import randint

arr = [0] * 5
linha = []
coluna = []

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
print('=' * 20)

print('Digite a linha e coluna que deseja trocar na matriz:')
while True:
    line = int(input('Linha -> '))
    if line not in range(5):
        print('Número de Linha Inválido!')
    else:
        break
while True:
    column = int(input('Coluna -> '))
    if column not in range(5):
        print('Número de Coluna Inválido!')
    else:
        break

for i in range(5):
    coluna.append(arr[i][column])
    linha.append(arr[line][i])

for i in range(5):
    arr[line][i] = coluna[i]
    arr[i][column] = linha[i]

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

print(linha)
print(coluna)
