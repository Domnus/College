from random import randint

arr = [0] * 5

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = i*j
        
print('Matriz:')
for i in range(5):
    for j in range(5):
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]', end='')
        else:
            print(f'[{arr[i][j]}]', end='')
    print()