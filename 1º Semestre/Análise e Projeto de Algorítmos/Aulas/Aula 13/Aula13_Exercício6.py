from random import randint

arr = [0] * 5
cont1 = 0
cont0 = 0

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = int(input())

for i in range(5):
    for j in range(5):
        if i == j:
            if arr[i][j] == 1:
                cont1 += 1
        if i != j:
            if arr[i][j] != 1:
                cont0 += 1

print('Matriz:')
print('=' * 20)
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 20)

if cont1 == 5:
    if cont0 == 20:
        print('Matriz Identidade')
else:
    print('Matriz Não Identidade')