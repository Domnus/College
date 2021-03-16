op = int(input("Digite 1 para a área do retângulo ou 2 para a área do triângulo: "))
base = float(input('Valor da base: '))
altura = float(input('Valor da altura: '))

if op != 1 or op != 2:
    print('Número inválido.')
elif op==1:
    area_retangulo = base*altura
    print(f'A área do retângulo será {area_retangulo}')
elif op==2:
    area_triangulo = (base*altura) / 2
    print(f'A área do triângulo será {area_triangulo}')
