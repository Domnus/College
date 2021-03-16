import math

A = float(input('Valor de A= '))
B = float(input('Valor de B= '))
C = float(input('Valor de C= '))

delta = (B**2) - 4*A*C

if A == 0:
    print('Não é equação de 2º grau.')
elif delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    raiz = (-B) / 2*A
    print(f'Raiz = {raiz}. Raiz única.')
else:
    raiz1 = ((-B) + math.sqrt(delta)) / 2*A
    raiz2 = ((-B) - math.sqrt(delta)) / 2*A
    print(f'Raizes: {raiz1} e {raiz2}')