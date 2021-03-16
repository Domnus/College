while True:
    h, w = input('Digite o tamanho da matriz: (0x0) -> ').split('x')
    h = int(h)
    w = int(w)
    if h <= 2 or w <= 2:
        print('!' * 47)
        print('!!A dimensão da matriz deverá ser maior que 2!!')
        print('!' * 47)
    else:
        break

S = ((h + (w**3)) / 2)
arr = [0] * h
soma_colunas = 0
soma_linhas = 0
soma_diagonal_principal = 0
soma_diagonal_secundaria = 0
cont1 = 0
cont2 = 0

print('Digite os valores da matriz:')
for i in range(h):
    arr[i] = [0] * w
    for j in range(w):
        arr[i][j] = int(input('-> '))

print('=' * 30)
print('Matriz:')
for i in range(h):
    for j in range(w):
        print(f'[{arr[i][j]}]',end= '')
    print()
print('=' * 30)

for i in range(h):
    for j in range(w):
        soma_linhas += arr[i][j]
    if soma_linhas == S:
        cont1 += 1
    soma_linhas = 0

for i in range(h):
    for j in range(w):
        soma_colunas += arr[j][i]
    if soma_colunas == S:
        cont2 += 1
    soma_colunas = 0

for i in range(h):
    for j in range(w):
        if i == j:
            soma_diagonal_principal += arr[i][j]

for i in range(h):
    for j in range(w):
        if j == (h - 1) - i:
            soma_diagonal_secundaria += arr[i][(h - 1)-i]

if cont1 == cont2:
    if soma_diagonal_principal == soma_diagonal_secundaria:
        print('Quadrado Mágico')
else:
    print('Não é um Quadrado Mágico')
print('=' * 30)
