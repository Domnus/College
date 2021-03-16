print('=-' * 20)
print('            Jogo da Velha')
print('=-' * 20)

player1 = input('Player 1-> ')
player2 = input('Player 2-> ')

game_rodando = True
vencedor = None

player_atual = 'X'

tabuleiro = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']
print('\nReady Player 1?')


def jogo():
    mostrar_tabuleiro()

    while game_rodando:
        turno()

        game_parou()

        trocar_player()
    if vencedor == 'X':
        print(f'Parabéns, o vencedor é o {player1}!')
    if vencedor == 'O':
        print(f'Parabéns, o vencedor é o {player2}!')
    elif vencedor == None:
        print('Jogo da Velha!')


def mostrar_tabuleiro():
    print('\n')
    print(f"       {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}      1 | 2 | 3")
    print(f"       {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}      4 | 5 | 6")
    print(f"       {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}      7 | 8 | 9")
    print()


def turno():
    print(f'É a vez do {player_atual}!')
    posicao = input('Escolha uma posição de 1 a 9-> ')

    valido = False
    while not valido:
        while posicao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            posicao = input('Escolha uma posição de 1 a 9-> ')
        posicao = int(posicao) -1
        if tabuleiro[posicao] != '-':
            print('Posição já ocupada! Escolha outra.')
        else:
            tabuleiro[posicao] = player_atual
            valido = True
        mostrar_tabuleiro()


def game_parou():
    se_vencedor()
    se_empate()


def se_vencedor():
    global vencedor
    diagonal_vencedor = diagonais()
    linha_vencedor = linhas()
    coluna_vencedor = colunas()

    if diagonal_vencedor:
        vencedor = diagonal_vencedor
    elif linha_vencedor:
        vencedor = linha_vencedor
    elif coluna_vencedor:
        vencedor = coluna_vencedor


def se_empate():
    global game_rodando
    if '-' not in tabuleiro:
        game_rodando = False
        return True
    else:
        return False


def diagonais():
    global game_rodando
    diagonal1 = tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != '-'
    diagonal2 = tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != '-'

    if diagonal1 or diagonal2:
        game_rodando = False
    if diagonal1:
        return tabuleiro[0]
    elif diagonal2:
        return tabuleiro[2]
    else:
        return None


def linhas():
    global game_rodando
    linha1 = tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != '-'
    linha2 = tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != '-'
    linha3 = tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != '-'

    if linha1 or linha2 or linha3:
        game_rodando = False
    if linha1:
        return tabuleiro[0]
    elif linha2:
        return tabuleiro[3]
    elif linha3:
        return tabuleiro[6]
    else:
        return None


def colunas():
    global game_rodando
    coluna1 = tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != '-'
    coluna2 = tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != '-'
    coluna3 = tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != '-'

    if coluna1 or coluna2 or coluna3:
        game_rodando = False
    if coluna1:
        return tabuleiro[0]
    elif coluna2:
        return tabuleiro[1]
    elif coluna3:
        return tabuleiro[2]
    else:
        return None


def trocar_player():
    global player_atual
    if player_atual == "X":
        player_atual = "O"
    elif player_atual == "O":
        player_atual = "X"


jogo()
