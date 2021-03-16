sexo = (input('Digite o sexo da pessoa: (M/F): '))
alt = float(input('Digite a altura da pessoa: '))

if sexo == 'M' or sexo == 'm':
    pi = (72.7 * alt) - 58
    print(f'O peso ideal será de {pi:.2f} kg.')
else:
    pi = (62.1 * alt) - 44.7
    print(f'O peso ideal será de {pi:.2f} kg.')