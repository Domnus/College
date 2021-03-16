frase = input('Enter sentence: ')

if len(frase) % 2 == 1:
    meio = int(len(frase) / 2)
    print(frase[meio])
elif len(frase) % 2 == 0:
    meio = int(len(frase) / 2)
    print(frase[meio-1],frase[meio])