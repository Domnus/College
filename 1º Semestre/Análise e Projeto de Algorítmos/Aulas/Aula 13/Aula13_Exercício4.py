from random import randint

arr = [0] * 8
cont = 0

for i in range(8):
    arr[i] = [0] * 8
    for j in range(8):
        arr[i][j] = (i+j) % 2

#for i in range(8):
#    for j in range(8):      
#        if i % 2 != 0 and j % 2 == 0:
#                arr[i][j] = 1
#        if i % 2 == 0 and j % 2 != 0:
#                arr[i][j] = 1

print('Matriz:')
print('=' * 24)
for i in range(8):
    for j in range(8):
        print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 24)  