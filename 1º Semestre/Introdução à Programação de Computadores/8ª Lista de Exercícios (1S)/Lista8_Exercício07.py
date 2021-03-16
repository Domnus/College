from random import randint

arr = [0] * 10
m = 0

for i in range(10):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(0, 10)

print('Matriz:')        
for i in range(10):
    for j in range(5):
        arr[i].sort()
        if arr[i][j] < 10:
            print(f'[0{arr[i][j]}]',end= '')
        else:
            print(f'[{arr[i][j]}]',end= '')
    print()

for i in range(10):
    soma = 0
    for j in range(1, 4):
        soma += arr[i][j]
    media = soma/3
    if media > m:
        m = media
        line = i
    
print(f'O vencedor foi o atleta Nº {line} com a média {m:.2f}')
    
        


