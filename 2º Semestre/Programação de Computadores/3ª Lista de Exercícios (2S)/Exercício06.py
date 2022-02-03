from random import randint

list = [0] * 10

def maiorColuna(coluna):
    maior = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j][coluna] > maior:
                maior = list[j][coluna]
    return maior

def maiorLinha(linha):
    maior = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[linha][j] > maior:
                maior = list[linha][j]
    return maior

for i in range(10):
    list[i] = [0] * 10
    for j in range(10):
        list[i][j] = randint(1, 50)

for i in range(10):
    for j in range(10):
        print("[{:2}]".format(list[i][j]), end='')
    print()


linha = int(input("Digite a linha: "))
coluna = int(input("Digite a coluna: "))

print(f"O maior número na linha {linha} é {maiorLinha(linha)}.")
print(f"O maior número na coluna {coluna} é {maiorColuna(coluna)}.")
