try:
    file = open(input("Informe o nome do arquivo: "), 'r')
    word = input('Informe a palavra que deseja procurar no arquivo: ')

    text = f.read()
    c = text.upper().count(word.upper())

    if c > 0:
        print(f'\"{word} foi encontrada {c} vezes no arquivo.')
    else:
        print('A palavra não foi encontrada!')
except:
    print('Arquivo não encontrado!')
