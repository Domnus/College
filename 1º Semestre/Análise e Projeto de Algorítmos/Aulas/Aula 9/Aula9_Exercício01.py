menor = 11
maior = 0

for i in range(1, 51):
    media = float(input('Digite a média-> '))
    if media >= 0 and media <=10:
        if media > maior:
            maior = media
        elif media < menor:
            menor = media
    else:
        print('Média Inválida!')

print(f'Média maior: {maior}.\nMédia menor: {menor}.')