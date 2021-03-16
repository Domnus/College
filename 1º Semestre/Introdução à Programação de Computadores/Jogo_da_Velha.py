op = 'S'
while op == 'S':
    sair = False
    matriz = ['1','2','3',
          '4','5','6',
          '7','8','9']

    print("Jogador 1 = X e Jogador 2 = O")

    sair = False
    player1 = input("Digite o nome do primeiro jogador: ")
    player2 = input("Digite o nome do segundo jogador: ")
    player_atual = 'X'
    nome = player1
    
    print()
    print(f'{matriz[0]} | {matriz[1]} | {matriz[2]}')
    print(f'{matriz[3]} | {matriz[4]} | {matriz[5]}')
    print(f'{matriz[6]} | {matriz[7]} | {matriz[8]}')
    print()
    while not sair:
        linha = int(input(nome + ", faça sua jogada: "))
        linha -= 1 
        if matriz[linha]  in ['1','2','3','4','5','6','7','8','9']:
            matriz[linha] = player_atual
        else:
            print("Jogada inválida, tente novamente !")
            continue
            
        print()
        print(f'{matriz[0]} | {matriz[1]} | {matriz[2]}')
        print(f'{matriz[3]} | {matriz[4]} | {matriz[5]}')
        print(f'{matriz[6]} | {matriz[7]} | {matriz[8]}')
        print()

        linha1 = matriz[0] == matriz[1] == matriz[2] not in ['1','2','3','4','5','6','7','8','9']
        linha2 = matriz[3] == matriz[4] == matriz[5] not in ['1','2','3','4','5','6','7','8','9']
        linha3 = matriz[6] == matriz[7] == matriz[8] not in ['1','2','3','4','5','6','7','8','9']

        if linha1 or linha2 or linha3:
            print(f'{nome} é o vencedor!')
            sair = True
            break

        coluna1 = matriz[0] == matriz[3] == matriz[6] not in ['1','2','3','4','5','6','7','8','9']
        coluna2 = matriz[1] == matriz[4] == matriz[7] not in ['1','2','3','4','5','6','7','8','9']
        coluna3 = matriz[2] == matriz[5] == matriz[8] not in ['1','2','3','4','5','6','7','8','9']

        if coluna1 or coluna2 or coluna3:
            print(f'{nome} é o vencedor!')
            sair = True
            break

        diagonal1 = matriz[2] == matriz[4] == matriz[6] not in ['1','2','3','4','5','6','7','8','9']
        diagonal2 = matriz[0] == matriz[4] == matriz[8] not in ['1','2','3','4','5','6','7','8','9']

        if diagonal1 or diagonal2:
            print(f'{nome} é o vencedor!')
            sair = True
            break

        if player_atual == 'X':
            player_atual = 'O'
            nome = player2
        elif player_atual == 'O':
            player_atual = 'X'
            nome = player1

        cont = 0

        for i in matriz:
            if i not in ['1','2','3','4','5','6','7','8','9']:
                cont += 1
            if cont == 9:
                print('Velha!')
                sair = True
    op = input('Deseja jogar novamente? [S/N] : ').upper()[0]
    