from random import randint

arr = [0] * 5

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(0, 9)

print('=' * 20)
print('Matriz:')
print('=' * 20)
for i in range(5):
    for j in range(5):
        print(f'[{arr[i][j]}]', end= '')
    print()

print('=' * 20)
print('Diagonal Principal:')
print('=' * 20)
for i in range(5):
    for j in range(5):
        if i == j:
            print(f'[{arr[i][j]}]', end='')
        else:
            print('[=]', end='')
    print()
print('=' * 20)

print('Diagonal Secundária: ')
print('=' * 20)
for i in range(5):
    for j in range(5):
        if j == 4 - i:
            print(f'[{arr[i][4-i]}]', end='')
        else:
            print('[=]', end='')
    print()
print('=' * 20)    