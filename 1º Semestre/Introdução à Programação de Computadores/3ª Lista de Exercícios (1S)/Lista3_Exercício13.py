x, y = (input('Informe os valores de X e Y: ')).split(',')
x = int(x)
y = int(y)

if x == 0 and y == 0:
    print('Ponto de origem.')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Quadrante 1.')
elif x < 0 and y > 0:
    print('Quadrante 2.')
elif x < 0 and y < 0:
    print('Quadrante 3.')
elif x > 0 and y < 0:
    print('Quadrante 4.')