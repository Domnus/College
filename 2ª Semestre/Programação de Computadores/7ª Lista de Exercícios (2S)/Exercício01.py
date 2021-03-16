tradutor = {}


def consulta(palavra):
    if tradutor == {}:
       return None
    else:
        if palavra not in tradutor:
            return False 
        return tradutor[palavra]

def adicionar(palavra, traducao):
    if palavra in tradutor or traducao in tradutor:
        print("Palavra já cadastrada!")
    else:
        try:
            tradutor[palavra] = traducao
            tradutor[traducao] = palavra
            return True
        except: 
            return False

def listagem():
    for x, y in tradutor.items():
        print(f"Palavra: {x} - Tradução: {y}")
def menu():
    print(f"-----Dicionário-----\n"
          f"-> 1. Consultar palavra\n"
          f"-> 2. Adicionar Palavra\n"
          f"-> 3. Listagem\n"
          f"-> 4. Sair do Programa")

    return input("Escolha a opção-> ")


while True:
    op = int(menu())
    if op == 1:
        x = input("Digite uma palavra para tradução: ")
        if consulta(x) == None:
            print("Tradutor vazio!")
        elif not consulta(x):
            print("Palavra inválida!")
        else:
            print(f"Tradução de {x}: {consulta(x)}")
    elif op == 2:
        p, t = input("Digita a palavra e a tradução que deseja inserir [PALAVRA, TRADUÇÃO] -> ").split(", ")
        if adicionar(p,t):
            print("Tradução adicionada com sucesso!")
        else:
            print("Erro na adição da tradução!")
    elif op == 3:
        listagem()
    elif op == 4:
        break
