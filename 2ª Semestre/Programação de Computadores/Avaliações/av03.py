# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

from colorama import Fore
from colorama import Style


def multmatriz(X, Y):
    c = [0] * len(X)
    for i in range(len(X)):
        c[i] = [0] * len(Y[0])
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                c[i][j] += (X[i][k] * Y[k][j])

    return c


def menu():
    print(f"{Fore.CYAN}-----Criptografia-----{Style.RESET_ALL}")
    print(f"{Fore.CYAN}-> 1. Criptografar    {Style.RESET_ALL}")
    print(f"{Fore.CYAN}-> 2. Descriptografar {Style.RESET_ALL}")
    print(f"{Fore.CYAN}-> 3. Sair do Programa{Style.RESET_ALL}")

    return int(input("Escolha a opção-> "))


def fraseEmNumero(frase):
    M = []
    global lista

    frase = list(frase)

    for i in range(len(frase)):
        if frase[i] in lista:
            j = lista.index(frase[i])
            M.append(j+1)

    if (len(M) / 2) % 2 != 0:
        M.append(30)

    return M


def numeroEmFrase(numeros):
    global lista
    bn = descriptografar(numeros)
    BN = []

    for i in range(len(bn)):
        for j in range(len(bn[i])):
            BN.append(bn[i][j])

    for i in range(len(BN)):
        BN[i] = lista[BN[i]-1]

    BN = ''.join(BN)

    return BN


def criptografar(frase):
    global A
    m = fraseEmNumero(frase)
    M = [[], []]
    N = [[], []]
    half = len(m) / 2
    M[0] = m[:int(half)]
    M[1] = m[int(half):]

    N = multmatriz(A, M)

    return N


def descriptografar(n):
    global B

    n = n.split(' ')

    while '' in n:
        n.remove('')

    for i in range(len(n)):
        n[i] = int(n[i])

    N = [[], []]
    half = len(n) / 2
    N[0] = n[:int(half)]
    N[1] = n[int(half):]
    BN = multmatriz(B, N)

    return BN


while True:
    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '!', '#', ' ']
    A = [[3, 1], [2, 1]]
    B = [[1, -1], [-2, 3]]
    x = menu()
    if x == 1:
        frase = input("Digite a frase-> ").upper().replace(' ', '#')
        N = criptografar(frase)
        print(f"{Fore.GREEN}Frase criptografada: {Style.RESET_ALL}")
        for i in range(len(N)):
            for j in range(len(N[i])):
                print(f"{Fore.GREEN} {N[i][j]}{Style.RESET_ALL}",
                      end=f'{Fore.GREEN} {Style.RESET_ALL}')
        print()
    elif x == 2:
        numeros = input(
            "Digite a frase criptografada no formato [NN, NN, NN]-> ")
        n = numeroEmFrase(numeros)
        print(f"{Fore.GREEN}Frase descriptografada: \n{n}{Style.RESET_ALL}")
    elif x == 3:
        break
    else:
        print(f"{Fore.RED}   _______________________{Style.RESET_ALL}")
        print(f"{Fore.RED}   |  Entrada Inválida!  |{Style.RESET_ALL}")
        print(f"{Fore.RED}   -----------------------{Style.RESET_ALL}")
