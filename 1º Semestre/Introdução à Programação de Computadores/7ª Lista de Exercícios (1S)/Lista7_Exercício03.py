from random import randint

arr = [0] * 10
soma = 0
arr_soma = []

for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = randint(1, 50)

for i in range(10):
    for j in range(10):
        soma += arr[i][j]
    arr_soma.append(soma)
    soma = 0

print('=' * 46)
print('Matriz:')
print('=' * 46)
for i in range(10):
    for j in range(10):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end= '')
        else:
            print(f'[{arr[i][j]}]', end= '')
    print(f'-> {arr_soma[i]}')
print('=' * 46)   


