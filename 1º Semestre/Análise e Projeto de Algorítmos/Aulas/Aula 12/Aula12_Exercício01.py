from random import randint
matriz = [0] * 5

for i in range(5):
    matriz[i] = [0] * 5
    for j in range(5):
        matriz[i][j] = randint(0, 9)

print('Matriz:')
for i in matriz:
    print(i)
print()

print('Diagonal Secundária: ')
for i in range(5):
    for j in range(5):
        if j == 4 - i:
            print(f'[{matriz[i][4-i]}]', end='')
        else:
            print('[=]', end='')
    print()
    