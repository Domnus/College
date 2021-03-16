from random import randint as rd

arr = [0] * 3
cont = 0

for i in range(3):
    arr[i] = [0] * 3
    for j in range(3):
        arr[i][j] = rd(1, 50)

for i in range(3):
    for j in range(3):
        print(f'[{arr[i][j]:2}]', end=' ')
    print()

for i in range(3):
    for j in range(3):
        if j == 2 - i:
            cont += arr[i][j]

print(f'A soma da diagonal secundária é {cont}')