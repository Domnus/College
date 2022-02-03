def menu():
    print('1 - Entrar com os dados\n'
          '2 - Locação\n'
          '3 - Devolução\n'
          '4 - Listagem\n'
          '5 - Sair\n')
    return input('Escola a opção -> ')

def entrada():
    while True:
            game.clear()
            game['codigo'] = input('Código do game: ')
            game['titulo'] = input('Título do game: ')
            game['situacao'] = 'D'
            locadora.append(game.copy())
            while True:
                a = input('Deseja continuar? S/N ').upper()
                if a in 'SN':
                    break
                print('Erro na entrada!')
            if a == 'N':
                break

def locacao():
    code = input('Digite o código do game: ')
    existe = False
    for jogo in locadora:
        if jogo['codigo'] == code:
            if jogo['situacao'] == 'A':
                print('Jogo não disponível para locação!')
            else:
                jogo['situacao'] = 'A'
                existe = True
                break
    if not existe:
        print('Jogo não encontrado!')

def devolucao():
    code = input('Digite o código do game: ')
    existe: False
    for jogo in locadora:
        if jogo['codigo'] == code:
            if jogo['situacao'] == 'A':
                jogo['situacao'] = 'D'
                print('Devolução realizada com sucesso!')
                existe = True
    if not existe:
       print('Jogo não cadastrado!')

def listagem():
    for jogo in locadora:
        for k, v in jogo.items:
            if k == 'codigo':
                print(f'Código = {v} ', end='')
            elif k == 'titulo':
                print(f'Título = {v} ', end='')
            elif k == 'situacao':
                if v == 'A':
                    print(f'Situação = Alugado ')
                else:
                    print(f'Situação = Disponível ')
locadora = list()
game = dict()

while True:
    op = int(menu())
    if op == 1:
        entrada()
    elif op == 2:
        locacao()
    elif op == 3:
        devolucao()
    elif op == 4:
        listagem()
    elif op == 5:
        break
    else:
        print('Entrada inválida!')

