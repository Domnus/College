# Bento Carlos Silva dos Santos RA: 600784
# Paulo Guilherme Astrauskas    RA: 548111

from math import sin, cos, radians

def getCentroQuadrado(forma):
    # 0---1 
    # |   | 
    # 2---3
    return ((forma[3][0]-forma[2][0])/2 + forma[0][0], (forma[1][1]-forma[3][1])/2 + forma[2][1])


def jogaProCentro(forma):  
    centro = getCentroQuadrado(forma)
    for i in range(len(forma)):
        forma[i][0] -= centro[0]
        forma[i][1] -= centro[1]
    return forma


def devolverProPontoOriginal(forma, centro):
    forma_devolvida = forma
    for i in range(len(forma)):
        forma_devolvida[i][0] += centro[0]
        forma_devolvida[i][1] += centro[1]
    return forma_devolvida


def transladar(forma, tx, ty):
    novaForma = forma
    for ponto in novaForma:
        ponto[0] += tx
        ponto[1] += ty
    return novaForma


def escalonar(forma, mx, my):
    centro = getCentroQuadrado(forma)
    forma_escalonada = jogaProCentro(forma)
    for i in range(len(forma)):
        forma_escalonada[i][0] *= mx
        forma_escalonada[i][1] *= my
    return devolverProPontoOriginal(forma_escalonada, centro)


def rotacionarPonto(ponto, angulo):
    angulo = radians(angulo)
    novoX = ponto[0] * cos(angulo) - ponto[1] * sin(angulo)
    novoY = ponto[0] * sin(angulo) + ponto[1] * cos(angulo)
    return [novoX, novoY]


def rotacionar(forma, angulo):
    centroForma = getCentroQuadrado(forma)
    formaNoCentro = jogaProCentro(forma)

    novaForma = []
    for ponto in formaNoCentro:
        novaForma.append(rotacionarPonto(ponto, angulo))

    return devolverProPontoOriginal(novaForma, centroForma)


def getQuadrado():
    print("Digite as coordenadas do quadrado:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))
    x4 = float(input("x4: "))
    y4 = float(input("y4: "))
    return [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]


def menuTranformacao(forma):
    print("Escolha uma transformação:")
    print("1 - Translação")
    print("2 - Escala")
    print("3 - Rotação")

    res = input("Opção: ")
    if res == "1":
        tx = float(input("Digite o valor de tx: "))
        ty = float(input("Digite o valor de ty: "))
        novaForma = transladar(forma, tx, ty)
        for ponto in novaForma:
            print("Nova coordenada: ", ponto)
    elif res == "2":
        mx = float(input("Digite o valor de mx: "))
        my = float(input("Digite o valor de my: "))
        novaForma = escalonar(forma, mx, my)
        for ponto in novaForma:
            print("Nova coordenada: ", ponto)
    elif res == "3":
        angulo = float(input("Digite o ângulo: "))
        novaForma = rotacionar(forma, angulo)
        for ponto in novaForma:
            print("Nova coordenada: ", ponto)
    else:
        print("Opção inválida!")


def menuFormas():
    print("Escolha uma forma:")
    print("1 - Quadrado")
    print("2 - Sair")

    res = input("Opção: ")
    if res == "1":
        forma = getQuadrado()
        menuTranformacao(forma)
    elif res == "2":
        exit(0)
    else:
        print("Opção inválida!")


menuFormas()