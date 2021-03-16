print('Digite a altura: ')
alt = float(input())
print('Digite o peso: ')
peso = float(input())

imc = peso/(alt**2)

if (imc < 18):
    print(f'Abaixo do peso. IMC = {imc}')
elif imc > 25:
    print(f'Peso normal. IMC = {imc}')
elif imc < 30:
    print(f'Acima do peso. IMC = {imc}')
else:
    print(f'Obeso(a). IMC = {imc}')
