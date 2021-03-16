frase = input('Enter sentence: ').lower()
character = input('Enter character: ').lower()

cont = 0

for i in frase:
    if i == character:
        cont += 1

print(f"O caractere '{character}' aparece {cont} vezes na frase")