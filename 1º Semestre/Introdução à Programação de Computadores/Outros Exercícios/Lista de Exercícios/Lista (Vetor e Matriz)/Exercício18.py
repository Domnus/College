from random import randint as rd

arr = [0] * 5
linha = None
coluna = None
for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = rd(1, 50)

x = rd(1, 50)

for i in range(5):
    for j in range(5):
        print(f'[{arr[i][j]:2}]', end=' ')
    print()

for i in range(5):
    for j in range(5):
        if arr[i][j] == x:
            linha = i
            coluna = j
        
            
if linha == None and coluna == None:
    print(f'O valor {x} não foi encontrado.')
else:
    print(f'O valor {x} está na linha {linha} e na coluna {coluna}')