from random import randint
m = []
print("           P1 P2 P3")
for i in range(10):
    m.append([])
    print("Aluno {:02}-> ".format(i+1),end="")
    for j in range(3):
        m[i].append(randint(0,10))
        print("{:2}".format(m[i][j]),end=" ")
    print()

piorP1 = piorP2 = piorP3 = 0
for i in range(10):
    if m[i][0]<=m[i][1] and m[i][0]<=m[i][2]:
        piorP1 += 1
    elif m[i][1]<=m[i][2]:
        piorP2 += 1
    else:
        piorP3 += 1
print("{} alunos tiveram a pior nota na Prova 1".format(piorP1))
print("{} alunos tiveram a pior nota na Prova 2".format(piorP2))
print("{} alunos tiveram a pior nota na Prova 3".format(piorP3))
