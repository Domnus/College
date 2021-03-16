from random import randint

arr = [0] * 5
linha1 = []
linha2 = []

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(1, 50)

print('Matriz:')
print('=' * 20)
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 20)

while True:
    print('Digite a linha e coluna que deseja trocar na matriz:')
    line1 = int(input('Linha 1 -> '))
    if line1 not in range(5):
        print('Número da linha inválido!')
    else:
        break

while True:
    print('Digite a linha e coluna que deseja trocar na matriz:')
    line2 = int(input('Linha 1 -> '))
    if line2 not in range(5):
        print('Número da linha inválido!')
    else:
        break

for i in range(5):
    if i == line1:
        linha1 = arr[i]
    if i == line2:
        linha2 = arr[i]

arr[line1] = linha2
arr[line2] = linha1

print('=' * 20)
print('Resultado:')
print('=' * 20)
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 20)



