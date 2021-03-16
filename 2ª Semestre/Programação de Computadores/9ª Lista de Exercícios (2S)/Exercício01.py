from os import close
from colorama import Fore
from colorama import Back
from colorama import Style
from random import Randint

def cadastrar(nome_arquivo, participantes, c):
    try:
        if c == 'cadastrar':
            file = open(nome_arquivo, "w+")
            for name in participantes:
                file.write(f'{name}\n')
        if c == 'adicionar':
            file = open(nome_arquivo, "a")
            file.write(f'{participantes[0]}\n')
    except:
        return 'Erro'


def sortear(arquivo):
    try:
        with file = open(arquivo, "r"):
             


def listarPessoas(arquivo):
    file = open(arquivo, "r")

    print(f"{Fore.BLUE}Participantes:")
    for line in file:
        print(line[:-1])

    print(f"{Style.RESET_ALL}")
    file.close


def listarDuplas():
    pass


def menu():
    print(f"-----Amigo Secreto-----\n"
          f"-> 1. Cadastrar Pessoas\n"
          f"-> 2. Sortear o amigo secreto\n"
          f"-> 3. Listas as pessoas cadastradas\n"
          f"-> 4. Listas as duplas sorteadas\n"
          f"-> 5. Encerrar")

    return input("Escolha a opção-> ")


while True:
    op = menu()
    if op == '1':
        c = 'cadastrar'
        while True:
            nome_arquivo = input("Digite o nome do arquivo: ")
            participantes = input("Digite o nome dos participantes: ").split()
            v = cadastrar(nome_arquivo, participantes, c)
            if v == 'Erro':
                print(f"{Back.RED}Ocorreu um erro!{Style.RESET_ALL}")
            else:
                print(f'{Back.BLUE}Nomes cadastrados com sucesso!{Style.RESET_ALL}')
            op = input("Deseja adicionar mais pessoas? [S/N]: ")[0].upper()
            if op == 'N':
                break
            else:
                c = 'adicionar'
    if op == '2':
        nome_arquivo = input("Digite o nome do arquivo: ")
        sortear(nome_arquivo)
    if op == '3':
        nome_arquivo = input('Digite o nome do arquivo: ')
        listarPessoas(nome_arquivo)
    if op == '4':
        pass
    if op == '5':
        print(f'{Fore.RED}O programa foi encerrado!{Style.RESET_ALL}')
        break
