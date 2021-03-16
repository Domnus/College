from random import randint

arr = [0] * 10

for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = randint(1, 50)

for i in range(10):
    arr[i].sort()
    
print('=' * 45)
print('Matriz:')
print('=' * 45)
for i in range(10):
    for j in range(10):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end= '')    
        else:
            print(f'[{arr[i][j]}]', end= '')
    print(f'-> {arr[i][0]}')
print('=' * 45)


