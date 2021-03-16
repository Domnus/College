#Observação:
# Para a letra a -> Colunas ímpares 1ª coluna(índice 0) 3ª coluna(índice 2) 5ª coluna(índice 4)
# Para a letra b -> Segunda e quarta colunas, índices 1 e 3
# Para a letra c -> Sexta coluna (índice 5) Colunas 1 e 2 (índices 0 e 1)
from random import randint
m = []
for i in range(3):
    m.append([])
    for j in range(6):
        m[i].append(randint(1,10))
        print("[{:2}]".format(m[i][j]),end="")
    print()

somaCI = 0
for i in range(3):
    for j in range(0,6,2):
        somaCI += m[i][j]
print("a) Soma de todos os elementos das colunas ímpares = ",somaCI)

somaC13 = 0
for i in range(3):
    somaC13 += m[i][1] + m[i][3]
print("b) Média de todos os elementos da segunda e quarta colunas = {:.2f}".format(somaC13/6))

for i in range(3):
    m[i][5] = m[i][0] + m[i][1]
print("c) Substituindo os valores da sexta coluna pela soma dos valores das colunas 1 e 2.")
print("d) A matriz ficou assim: ")
for i in range(3):
    for j in range(6):
        print("[{:2}]".format(m[i][j]),end="")
    print()