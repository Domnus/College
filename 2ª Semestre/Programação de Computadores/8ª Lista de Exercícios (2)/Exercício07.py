try:
    entrada = open(input('Arquivo de entrada: '), 'r')
    saida = open(input('Arquivo de saída: '), "w+", enconding="utf-8")
    maior = 0

    for cidades in entrada:
        dados = cidades.split()
        pop = int(dados[-1])
        if pop > maior:
            maior = pop
            mdados = cidades
    saida.write(mdados)
    entrada.close()
    saida.seek(0)
    print(saida.read())
    saida.close()
except IOError:
    print('Arquivo não encontrado!')

