from random import randint

arr = [0] * 4
arrT = [0] * 6

for i in range(4):
    arr[i] = [0] * 6
    for j in range(6):
        arr[i][j] = randint(0, 9)

for i in range(6):
    arrT[i] = [0] * 4

print('=' * 18) 
print('Matriz:')
for i in range(4):
    for j in range(6):
        print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 18) 

for i in range(4):
    for j in range(6):
        arrT[j][i] = arr[i][j]

print('Matriz Transposta:')
for i in range(6):
    for j in range(4):
        print(f'[{arrT[i][j]}]', end= '')
    print()
print('=' * 18) 