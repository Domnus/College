from random import randint

arr = [0] * 10
m_d = []
line = []

for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = randint(1, 50)

print('Matriz:')
print('=' * 40)
for i in range(10):
    for j in range(10):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 40)

linha = int(input('Digite o número da linha desejada -> '))
for i in range(10):
    if i == linha:
            line.append(arr[i])

print(f'Linha {linha}:')
print(line)
print('=' * 40)