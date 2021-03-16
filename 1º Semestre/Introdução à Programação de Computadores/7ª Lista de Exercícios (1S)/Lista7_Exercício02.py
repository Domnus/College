from random import randint

arr = [0] * 10
soma = 0
dividendo = 0

for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = randint(1, 50)

print('=' * 40)
print('Matriz:')
for i in range(10):
    for j in range(10):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end= '')
        else:
            print(f'[{arr[i][j]}]', end= '')
    print()
print('=' * 40)

for i in range(10):
    for i in range(10):
        soma += arr[i][j]
        dividendo += 1

m_arr = soma / dividendo

print(f'A média dos elementos da matriz será {m_arr}')