from random import randint

arr = [0] * 4
arrT = [0] * 6

print('Informe os valores da matriz:')
for i in range(4):
    arr[i] = [0] * 6
    for j in range(6):
        arr[i][j] = int(input('-> '))

print('Matriz:')
print('=' * 24)
for i in range(4):
    for j in range(6):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 24)

for i in range(6):
    arrT[i] = [0] * 4
    for j in range(4):
        arrT[i][j] = 0

for i in range(4):
    for j in range(6):
        arrT[j][i] = arr[i][j]

print('Matriz Tranversa:')
print('=' * 24)
for i in range(6):
    for j in range(4):
        if arrT[i][j] < 10:
            print(f'[0{arrT[i][j]}]', end='')
        else:
            print(f'[{arrT[i][j]}]', end='')
    print()
print('=' * 12)



