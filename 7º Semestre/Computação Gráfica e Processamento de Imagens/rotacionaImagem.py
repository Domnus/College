#!/usr/bin/env python3

from PIL import Image
import numpy as np

try:
    def invertArray(array):
        newArray = []
        for i in range(len(array) - 1, -1, -1):
            newArray.append(array[i])
        return newArray
        
    def inverter90Esquerda(imgArray, newImg):
        for i in range(len(imgArray)):
            # Transforma a linha em array e inverte
            row = imgArray[i].tolist()
            rowInverted = invertArray(row)
            for j in range(len(rowInverted)):
                newImg.putpixel((i, j), tuple(rowInverted[j]))

    def inverter90Direita(imgArray, newImg):
        contW = newImg.width - 1
        for i in range(len(imgArray)):
            # Transforma a linha em array e inverte
            row = imgArray[i].tolist()
            rowInverted = invertArray(row)
            for j in range(len(rowInverted)):
                newImg.putpixel((contW, j), tuple(rowInverted[j]))
            contW -= 1

    def menu(imgArray, newImg):

        print("Inverter 90º para a esquerda (1)")
        print("Inverter 90º para a direita (2)")

        res = input("Digite a opção desejada: ")
        if res == "1":
            inverter90Esquerda(imgArray, newImg)
        elif res == "2":
            inverter90Direita(imgArray, newImg)
        else:
            print("Opção inválida")
            menu(imgArray, newImg)


    # Carrega a imagem
    img = Image.open("img.jpg")
    # img = Image.open("./teste.png")
    # Pega as dimensões da imagem
    width, height = img.size
    # Cria a imagem nova
    newImg = Image.new(mode="RGB", size=(height, width))

    width, height = newImg.size
    # Transforma a imagem em array
    imgArray = np.asarray(img)

    menu(imgArray, newImg)

    # Salva a imagem
    newImg.save("imagemRotacionada.png")
    newImg.show()

except IOError:
    print("Erro ao carregar a imagem")
    exit(1)
