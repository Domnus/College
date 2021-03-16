vogais = ('a', 'e', 'i', 'o', 'u')
cont = 0

frase = input('Enter sentence: ').lower()

for i in frase:
    if i in vogais:
        cont += 1

print(f'A frase tem {cont} vogais')


