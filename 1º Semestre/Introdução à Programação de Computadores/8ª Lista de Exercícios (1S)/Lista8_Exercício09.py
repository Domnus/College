from random import randint

arr = [0] * 9

for i in range(9):
    arr[i] = [0] * 9
    for j in range(9):
        arr[i][j] = randint(0, 10)

print('Matriz:')  
print('=' * 36)      
for i in range(9):
    for j in range(9):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]',end= '')
        else:
            print(f'[{arr[i][j]}]',end= '')
    print()
print('=' * 36)

while True:
    quadrante = int(input('Digite o quadrando desejado: '))
    if quadrante not in range(1, 5):
        print('Número inválido! Digite um número entre 1 e 4')
    else:
        break

print('=' * 16)    
if quadrante == 1:
    for i in range(4):
        for j in range(5, 9):
            if arr[i][j] < 10:
                print(f'[0{arr[i][j]}]',end= '')
            else:
                print(f'[{arr[i][j]}]',end= '')
        print()
if quadrante == 2:
    for i in range(4):
        for j in range(4):
            if arr[i][j] < 10:
                print(f'[0{arr[i][j]}]',end= '')
            else:
                print(f'[{arr[i][j]}]',end= '')
        print()
if quadrante == 3:
    for i in range(5, 9):
        for j in range(4):
            if arr[i][j] < 10:
                print(f'[0{arr[i][j]}]',end= '')
            else:
                print(f'[{arr[i][j]}]',end= '')
        print()
if quadrante == 4:
    for i in range(5, 9):
        for j in range(5, 9):
            if arr[i][j] < 10:
                print(f'[0{arr[i][j]}]',end= '')
            else:
                print(f'[{arr[i][j]}]',end= '')
        print()

print('=' * 16)