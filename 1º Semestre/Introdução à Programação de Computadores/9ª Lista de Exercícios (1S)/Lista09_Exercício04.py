frase = input('Enter sentence: ').lower()
character = input('Enter character: ').lower()
character2 = input('Enter character: ').lower()

cont = 0

for i in range(len(frase)):
    if frase[i] == character.lower() or frase[i] == character2.upper():
        cont += 1

frase = frase.replace(character, character2)
print(f'Nova frase: {frase}')
print(f'O caractere {character} foi substituído {cont} vezes')