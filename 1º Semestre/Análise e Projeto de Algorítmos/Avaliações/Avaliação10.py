from random import randint
matriz = [0] * 5
soma = 0

for i in range(5):
    matriz[i] = [0] * 5
    for j in range(5):
        matriz[i][j] = randint(0, 9)

for i in matriz:
    print(i)

for i in range(5):
    for j in range(5):
        soma += matriz[i][j]
    print(f'Soma da {i + 1}ª linha = {soma}')
    soma = 0

print()
soma = 0
for i in range(5):
    for j in range(5):
        soma += matriz[j][i]
    print(f'Soma da {i + 1}ª coluna = {soma}')
    soma = 0
        

 
