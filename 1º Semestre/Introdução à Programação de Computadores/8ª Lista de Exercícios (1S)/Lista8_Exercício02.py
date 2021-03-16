from random import randint

arr = [0] * 10
m_d = []

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

for i in range(10):
    for j in range(10):
        if i == j:
            m_d.append(arr[i][j])

print('Diagonal Principal:')
print(m_d)
print('=' * 40)