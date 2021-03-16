from random import randint

arr = [0] * 5
sim = True

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(0, 50)

print('Matriz:')
print('=' * 15)
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 15)

for i in range(5):
    for j in range(5):
        if arr[i][j] != arr[j][i]:
            sim = False
            break

if sim:
    print('Matriz Simétrica')
else:
    print('Matriz Não Simétrica')


