dist = float(input('Distância em KM: '))
litros = float(input('Litros consumidos: '))

consumo = dist / litros

if consumo < 8:
    print('Venda o carro.')
elif consumo > 8 and consumo < 14:
    print('Econômico.')
else:
    print('Super Econômico.')