arr = [0] * 8
board = {'A':0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H':7}

for i in range(8):
    arr[i] = [0] * 8
    
while True:
    y, letra = input('Informe as coordenadas da Torre [1 a 8],[A a H] -> ').split(',')
    letra = letra.upper()
    x = board[letra]
    y = int(y) - 1
    if x not in range(8) or y not in range(8):
        print('Coordenadas erradas! Digite um valor entre 0 e 7!')
    else:
        break

for i in range(8):
    for j in range(8):
        arr[i][j] = ' '

for i in range(8):
    for j in range(8):
        if i + j == x + y or i - j == y - x:
            arr[i][j] = 'X'
        if arr[i][j] == arr[y][x]:
            arr[y][x] = 'B'

for i in range(8):
    for j in range(8):
        print(f'[{arr[i][j]}]', end= '')
    print()