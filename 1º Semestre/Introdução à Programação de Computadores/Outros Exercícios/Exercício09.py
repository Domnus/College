soma = 0
notas = []

print('Digite uma nota inválida para parar o programa.')

while True:
    x = float(input('Nota -> '))
    if x < 0 or x > 10 or:
        break
    else:
        soma += x
        notas.append(x)

media = soma / len(notas)

print(f'A média é {media:.3f}')
