from random import randint

arr = [0] * 10

for i in range(10):
    arr[i] = [0] * 3
    for j in range(3):
        arr[i][j] = randint(1, 9)

print('Matriz:')
for i in range(10):
    num = arr[i][0]
    cont = 0
    for j in range(3):
        print(f'[{arr[i][j]}]', end='')
        if arr[i][j] == num:
            cont += 1
    if cont == 3:
        print(' -> Equilátero')
    elif cont == 2:
        print(' -> Isósceles')
    else:
        print(' -> Escaleno')
     
