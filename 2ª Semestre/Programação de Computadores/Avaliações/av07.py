# Alisson Juan Feitoza---------RA: 601081
# Andressa Caroline R. Bueno---RA: 607290
# Bento Carlos S. dos Santos---RA: 600784
# Fernando Cremonez Costa------RA: 604097
# Frederico Hanai--------------RA: 604593
# Hugo Seiti Odajima-----------RA: 606537

from colorama import Fore
from colorama import Back
from colorama import Style

def cadastroCantores():
    cantor = input("- Cantor: ").upper().strip()
    if cantor in cantores.keys():
        print(f"{Back.RED}Cantor já cadastrado!{Style.RESET_ALL}")
    else:
        codigo = input("- Código: ").strip()
        if cantor in cantores.keys():
            print(f"{Back.RED}Cantor já cadastrado!{Style.RESET_ALL}")
        while codigo in cantores.values():
            print(f"{Back.RED}Código já cadastrado!{Style.RESET_ALL}")
            codigo = input("- Insira outro código: ")
        else:
            cantores[cantor] = codigo
            print(f"{Back.BLUE}Cadastro Realizado com Sucesso!{Style.RESET_ALL}")

def listagemCantores():
    if cantores == {}:
        print(f"{Back.RED}Nenhum cantor cadastrado!{Style.RESET_ALL}")
    else:
        print("  Cantores cadastrados: ")
        print("============================")
        for cantor, codigo in cantores.items():
            print(f"{Fore.BLUE}Cantor -> {cantor}{Style.RESET_ALL}")
            print(f"{Fore.BLUE}Código -> {codigo}{Style.RESET_ALL}")
            print("============================")

def consultaCantores(x, op):
    existe = False
    if op == "Key":
        for i in cantores.keys():
            if x == i:
                existe = True
                break
        return (existe, x)
    else:
        for i in cantores.values():
            if x == i:
                existe = True
                break
        return existe

def cadastroMusica():
    nomeMusica = input("- Nome da música: ").lower().strip()
    if nomeMusica not in musicas.keys():
        codigoCantor = input("- Código do cantor: ").strip()
        estiloMusica = input("- Estilo da música: ").strip()
        if consultaCantores(codigoCantor, "Value"):
          for nomeCantor, codigo in cantores.items():
              if codigo == codigoCantor:
                  musicas[nomeMusica] = (nomeCantor, estiloMusica)
                  print(f"{Back.BLUE}Cadastro Realizado com Sucesso!{Style.RESET_ALL}")
        else:
            print(f"{Back.RED}Cantor não cadastrado!{Style.RESET_ALL}")
    else:
        print(f"{Back.RED}Música já cadastrada!{Style.RESET_ALL}")

def listagemMusica():
    if musicas == {}:
        print(f"{Back.RED}Nenhuma música cadastrada!{Style.RESET_ALL}")
    else:
        print("  Músicas cadastradas: ")
        print("============================")
        for nomeMusica, cantor in musicas.items():
              print(f"Cantor: {cantor[0]}\n"
                    f"Nome da música: {nomeMusica}\n"
                    f"Estilo: {cantor[1]}\n"
                     "============================")

def consultaMusica(nomeMusica):
    if nomeMusica in musicas.keys():
        cantor, estilo = musicas[nomeMusica]
        print(f"{Fore.BLUE}Cantor: {cantor} | Estilo: {estilo}{Style.RESET_ALL}")
    else:
        print(f"{Back.RED}Música não cadastrada!{Style.RESET_ALL}")

def gerarPlaylistMusica():
    playlist = list()
    nomeMusica = ''
    while True:
        nomeMusica = input("- Digite a música de escolha ou FIM para encerrar-: ").lower().strip()
        if nomeMusica.upper() == "FIM":
            break
        else:
            if nomeMusica in musicas.keys():
                playlist.append(nomeMusica)
    if playlist != []:
        print(f"{Back.BLUE}Playlist montada com sucesso!{Style.RESET_ALL}")
        for musica in playlist:
            print(f"{Fore.BLUE}{musica}{Style.RESET_ALL}")
    else:
        print(f"{Back.RED}Nenhuma música foi cadastrada!{Style.RESET_ALL}")

def gerarPlaylistCantor(nomeCantor):
    playlist = list()
    if nomeCantor in cantores:
        for musica, cantor in musicas.items():
            if nomeCantor == cantor[0]:
                playlist.append(musica)
        if playlist != []:
            print(f"{Back.BLUE}Playlist montada com sucesso!{Style.RESET_ALL}")
            for musica in playlist:
                print(f"{Fore.BLUE}{musica}{Style.RESET_ALL}")
        else:
            print(f"{Back.RED}Playlist vazia!{Style.RESET_ALL}")

def entradaInvalida():
    print(f"{Fore.RED}_______________________\n"
                    f"|  Entrada Inválida!  |\n"
                    f"-----------------------{Style.RESET_ALL}")

def menu():
    print(f"{Fore.GREEN}-----------------------\n"
                      f"       Pie Music       \n"
                      f"-----------------------\n"
                      f"1. Cantor\n"
                      f"2. Música\n"
                      f"3. Playlist\n"
                      f"4. Sair{Style.RESET_ALL}")
    return input("- Escolha a opção -> ").strip()

cantores = dict()
musicas  = dict()

while True:
    op = menu()
    if op == '1':
        while True:
            print(f"{Fore.MAGENTA}============================\n"
                                f"           Cantor           \n"
                                f"============================\n"
                                f"a. Cadastro de Cantores\n"
                                f"b. Listagem de Cantores\n"
                                f"c. Consulta de Cantores\n"
                                f"d. Voltar{Style.RESET_ALL}")
            op = input("- Escolha a opção -> ").lower().strip()
            if op == 'a':
                cadastroCantores()
            elif op == 'b':
               listagemCantores()
            elif op == 'c':
               cantor = input("- Digite o cantor que deseja consultar: ").upper().strip()
               x = consultaCantores(cantor, "Key")
               if x[0]:
                   print(f"{Back.GREEN}Código do cantor: {cantores[x[1]]}{Style.RESET_ALL}")
               else:
                   print(f"{Back.RED}Cantor não cadastrado!{Style.RESET_ALL}")
                   op2 = input(f"- Deseja cadastrá-lo? S/N : ").upper().strip()
                   if op2 in "SN":
                       if op2 == "S":
                           cadastroCantores()
                       else:
                            break
                   else:
                       entradaInvalida()
            elif op == 'd':
                break
            else:
                entradaInvalida()
    elif op == '2':
            while True:
                print(f"{Fore.CYAN}============================\n"
                                 f"           Música           \n"
                                 f"============================\n"
                                 f"a. Cadastro de Músicas\n"
                                 f"b. Listagem de Músicas\n"
                                 f"c. Consulta de Músicas\n"
                                 f"d. Voltar{Style.RESET_ALL}")
                op = input("Escolha a opção -> ").lower().strip()
                if op == 'a':
                    cadastroMusica()
                elif op == 'b':
                    listagemMusica()
                elif op == 'c':
                    nomeMusica = input("- Digite o nome da música: ").lower().strip()
                    consultaMusica(nomeMusica)
                elif op == 'd':
                    break
                else:
                    entradaInvalida()
    elif op == '3':
            while True:
                print(f"{Fore.YELLOW}============================\n"
                                   f"           Playlist         \n"
                                   f"============================\n"
                                   f"a. Playlist por música\n"
                                   f"b. Playlist por cantores\n"
                                   f"c. Voltar{Style.RESET_ALL}")
                op = input("- Escolha a opção -> ").lower().strip()
                if op == 'a':
                    gerarPlaylistMusica()
                elif op == 'b':
                    nomeCantor = input("- Digite o nome do cantor-> ").upper().strip()
                    gerarPlaylistCantor(nomeCantor)
                elif op == 'c':
                    break
                else:
                    entradaInvalida()
    elif op == '4':
        print(f"{Fore.RED}Programa finalizado!{Style.RESET_ALL}")
        break
    else:
        entradaInvalida()
