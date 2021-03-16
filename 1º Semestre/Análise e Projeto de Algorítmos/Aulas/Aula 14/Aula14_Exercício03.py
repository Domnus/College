tab = [] *  8
cont = 1
lista = ['a','b','c','d','e','f','g','h']
for i in range(0,8):
    tab.append([])
    print(' {}'.format(i),end=' ')
print()
for i in range(0,8):
    print('{}'.format(i+1),end='')
    for j in range(0,8):
        print('[ ]',end='')
    print()
while True:
    x,y = input('Insira a posição que o cavalo sera inserido(letra,numero) - > ').split(',')
    y = int(y) - 1
    if x in lista and 0 <=  y <= 7:
        break
for i in lista:
    if i == x:
        x = lista.index(i)
for i in range(0,8):
    for j in range(0,8):
        if j == x and i == y:
            print('[{:3}]'.format(' C'),end='')
        elif (j == x+2 and i == y+1) or (j == x+1 and i == y+2) or (j == x-2 and i == y-1) or (j == x-1 and i == y-2) or (j == x+1 and i == y-2) or (j == x-2 and i == y+1) or (j == x-1 and i == y+2) or (j == x+2 and i == y-1):
            print('[{:3}]'.format(' X'), end='')

        else:
            print('[{:3}]'.format(''),end='')
    print()