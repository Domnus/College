from random import randint as rd

arr = [0] * 5
soma = 0

for i in range(5):
    arr[i] = [0] * 10
    for j in range(5):
        arr[i][j] = rd(1, 50)

print('=' * 35)
for i in range(5):
    for j in range(5):
        print(f'[{arr[i][j]:2}]', end='')
        soma += arr[i][j]
    print(f'  Linha {i+1} = {soma}', end='') 
    soma = 0           
    print()
print('=' * 35)