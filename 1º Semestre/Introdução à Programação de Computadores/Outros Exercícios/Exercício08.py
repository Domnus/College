altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

if altura < 1.20:
    if peso < 60:
        print('Classificação A')
    elif peso > 60 and peso < 90:
        print('Classificação D')
    elif peso > 90:
        print('Classificação G')
elif altura < 1.70 and altura > 1.20:
    if peso < 60:
        print('Classificação B')
    elif peso > 60 and peso < 90:
        print('Classificação E')
    elif peso > 90:
        print('Classificação H')
elif altura > 1.70:
    if peso < 60:
        print('Classificação C')
    elif peso > 60 and peso < 90:
        print('Classificação F')
    elif peso > 90:
        print('Classificação I')  
