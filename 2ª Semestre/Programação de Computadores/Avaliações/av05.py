# Alisson Juan Feitoza RA: 601081
# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

from colorama import Fore
from colorama import Back
from colorama import Style

def insercao(cor, codigo):
    cores.append((cor,codigo))

def consulta(nomeCor):
    v = [("True", cor[1]) for cor in cores if cor[0] == nomeCor]
    return v

def listagem():
    if cores == []:
        print(f"{Back.RED}Lista vazia!{Style.RESET_ALL}")
    else:
        for i, cor in enumerate(cores):
            print(f"{Fore.CYAN}{i+1}º: Cor-> {cor[0]} \n"
                  f"    Código-> {cor[1]}{Style.RESET_ALL}")

def menu():
    print(f"{Fore.WHITE}-----Cores em {Back.RED}R{Back.GREEN}G{Back.CYAN}B{Style.RESET_ALL}{Fore.WHITE}-----\n"
          f"-> 1. Inserção\n"
          f"-> 2. Consulta\n"
          f"-> 3. Listagem\n"
          f"-> 4. Sair do Programa{Style.RESET_ALL}")

    return input("Escolha a opção-> ")

cores = []
while True:
    try:
        op = int(menu())
        if op == 1:
            cor, codigo = input("Digite a cor e o código RGB separados por um espaço: ").split()
            insercao(cor.upper(), codigo.lower())
            print(f"{Fore.GREEN}Inserção realizada com sucesso!{Style.RESET_ALL}")
        elif op == 2:
            nomeCor = str(input("Insira o nome da cor-> ")).upper()
            validacao = consulta(nomeCor)

            try:
                if validacao[0][0] == "True":
                    print(f"{Fore.GREEN}Cor válida.\nCódigo da cor: {validacao[0][1]}{Style.RESET_ALL}")
                else:
                    print(f"{Back.RED}Cor inválida{Style.RESET_ALL}")
            except:
                print(f"{Back.RED}Cor inválida{Style.RESET_ALL}")
        elif op == 3:
            listagem()
        elif op == 4:
            print(f"{Fore.RED}O programa foi encerrado.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}_______________________{Style.RESET_ALL}")
            print(f"{Fore.RED}|  Entrada Inválida!  |{Style.RESET_ALL}")
            print(f"{Fore.RED}-----------------------{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}_______________________{Style.RESET_ALL}")
        print(f"{Fore.RED}|  Entrada Inválida!  |{Style.RESET_ALL}")
        print(f"{Fore.RED}-----------------------{Style.RESET_ALL}")
