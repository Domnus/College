vogais = ['A', 'E', 'I', 'O', 'U']
cont = 0

frase = input('Digite uma frase: ')
l = list(frase)

for i in l:
    x = i.upper()
    if x in vogais:
        cont += 1

print(f'A frase tem {cont} vogais.')
