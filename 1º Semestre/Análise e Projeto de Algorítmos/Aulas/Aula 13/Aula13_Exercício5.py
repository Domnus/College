from random import randint

arr = [0] * 5
linha = 0
maior = 0
minimax = 50

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(0, 50)

for i in range(5):
    for j in range(5):
        if arr[i][j] > maior:
            maior = arr[i][j]
            linha = i

for i in arr[linha]:
    if i < minimax:
        minimax = i

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

print(f'O maior número da matriz é {maior}')
print(f'O minimax da matriz é {minimax} e se encontra na linha {linha + 1}')