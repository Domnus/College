from random import randint

arr = [0] * 10

for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = randint(1, 50)

print('=' * 40)
print('Matriz:')
print('=' * 40)
for i in range(10):
    for j in range(10):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end= '')
        else:
            print(f'[{arr[i][j]}]', end= '')
    print()
print('=' * 40)

for i in range(0, 10):
    minm = arr[0][i]
    for j in range(10):
        if (arr[j][i] < minm):
            minm = arr[j][i]
    print(f' {i+1}ª coluna: {minm} ', end=' ')
    print()
print('=' * 40)
 