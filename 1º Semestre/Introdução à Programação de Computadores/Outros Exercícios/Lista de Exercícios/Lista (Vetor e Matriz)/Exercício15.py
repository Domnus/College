from random import randint as rd

arr = [0] * 4
cont = 0

for i in range(4):
    arr[i] = [0] * 4
    for j in range(4):
        x = rd(1, 36)
        if x > 10:
            cont += 1
            arr[i][j] = x

for i in range(4):
    for j in range(4):
        print(f'[{arr[i][j]:2}]', end=' ')
    print()

print(f'Há {cont} valores maiores que 10 na matriz')


