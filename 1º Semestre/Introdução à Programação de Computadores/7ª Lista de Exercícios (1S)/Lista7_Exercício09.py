from random import randint 

arr = [0] * 10
cont = 0

for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = randint(0, 9)

print('=' * 30)
print('Matriz:')
print('=' * 30)
for i in range(10):
    for j in range(10):
        print(f'[{arr[i][j]}]', end= '')
    print()
print('=' * 30)

for i in range(10):
    for j in range(10):
        if arr[i][j] == arr[j][i]:
            cont += 1

if cont == 100:
    print('Matriz Simétrica')
else:
    print('Matriz não Simétrica')
print('=' * 30)

