from random import randint as rd

arr = [0] * 10
maior = 0
for i in range(10):
    arr[i] = [0] * 10
    for j in range(10):
        arr[i][j] = rd(1, 99)

for i in range(10):
    for j in range(10):
        if arr[i][j] > maior:
            maior = arr[i][j]
            linha = i
            coluna = j
    menor = maior

for i in range(10):
    for j in range(10):
        if arr[i][j] <10:        
            print(f'0{arr[i][j]}', end= ' ')
        else:
            print(f'{arr[i][j]}', end=" ")
    print()

for i in arr[linha]:
    if i < menor:
        menor = i

print(f'Minimax= {menor} \nLinha= {linha}\nColuna= {coluna}')


    