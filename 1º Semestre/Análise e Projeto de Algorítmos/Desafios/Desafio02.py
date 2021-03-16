from random import randint

desafio = True
arr = []
imagem = []
while desafio:
    print('------Menu------')
    print('1 – Inserir a imagem (criar a matriz (max. 20x20) \n2 – Compactar a imagem \n3 – Descompactar a imagem \n4 – Sair do programa')
    inp = int(input('-> '))
    if inp == 1:
        h, w = input('Digite o tamanho da imagem [HxW] -> ').split('x')
        h = int(h)
        w = int(w)
        if h > 20 or w > 20:
            print('A matriz não deve ultrapassar 20x20')
        else:
            print('Digite os valores da matriz:')
            imagem = [0] * h
            for i in range(h):
                imagem[i] = [0] * w
                cond = 0
                while cond < w:
                    x = randint(0, 1)
                    if x != 0 and x != 1:
                        print('Digite apenas 1 ou 0!')
                    else:
                        imagem[i][cond] = x
                        cond += 1
        print('=' * len(imagem) * 2)        
        for i in range(h):
            for j in range(w):
                print(f'{imagem[i][j]}', end=' ')
            print()
        print('=' * len(imagem) * 2) 
    elif inp == 2:
        if not imagem:
            print('=' * 39)
            print('=Primeiro digite os valores da matriz!=')
            print('=' * 39)
            continue
        else:
            compactacao = []
            print('Matriz compactada:')
            for i in range(h):
                p, b = 0, 0
                for j in range(w):
                    if(imagem[i][j] == 1):
                        p += 1
                    if(imagem[i][j] == 0):
                        b += 1
                    if j == w-1 or imagem[i][j] != imagem[i][j+1]:
                        if(p>0):
                            compactacao.append(f'{p}P')
                        elif(b>0):
                            compactacao.append(f'{b}B')    
                        p, b = 0, 0
                compactacao.append('0')
            compactacao.append('0')
            for i in range(len(compactacao)):
                print(compactacao[i], end='')
            print()
            byte_imagem = h * w
            byte_imagem_compactada = len(compactacao)
            bytes_economizados = byte_imagem - byte_imagem_compactada
            print(f"Foram economizados {bytes_economizados} bytes!")
    elif inp == 3:
        arr = [[]]
        cont = 0
        linhas = 1
        linha_w = 0
        print('Digite o vetor da imagem compactada:')            
        imagem_compactada = input("-> ")
        for character in imagem_compactada:
            if character.isdecimal():
                numero = int(character)
            else:
                letra = character
            if numero == 0:
                arr.append([])
                cont += 1
                linhas += 1
                continue
            try:
                if letra == 'B':
                    for i in range(numero):
                        arr[cont].append(0)
                elif letra == 'P':
                    for i in range(numero):
                        arr[cont].append(1)
                letra = ''
            except Exception:
                pass
        
        for i in range(1):
            arr.pop()     
        
        linha_w = len(arr[0])
        print('Imagem:')
        print('=' * linha_w * 2)
        for i in range(linhas - 2):
            for j in range(len(arr[i])):
                print(f'{arr[i][j]}', end=' ')
            print()
                    
        print('=' * linha_w * 2)
    
    elif inp == 4:
        print('Programa Encerrado')
        desafio = False
                      