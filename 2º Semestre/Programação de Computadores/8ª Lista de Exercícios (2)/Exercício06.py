try:
    entrada = open(input('Informe o nome do arquivo: '), 'r')
    saida = open("idades.txt", "w+")
    anoAtual = int(input('Ano atual:'))

    for pessoa in entrada:
        dados = pessoa.split()
        anoNasc = int(dados[-1])
        idade = anoAtual - anoNasc
        saida.write(f"{dados[0]} - Idade: {idade}\n")

    entrada.close()
    saida.seek(0)
    print(saida.read())
except IOError:
    print('Arquivo não encontrado!')
