#!/usr/bin/env python3

from PIL import Image
import numpy as np

try:
    def invertArray(array):
        newArray = []
        for i in range(len(array) - 1, -1, -1):
            newArray.append(array[i])
        return newArray

    # Carrega a imagem
    # img = Image.open("./teste.png")
    img = Image.open("./img.jpg")
    # Pega as dimensões da imagem
    width, height = img.size

    # Cria a imagem nova
    newImg = Image.new(mode="RGB", size=(width, height))

    # Transforma a imagem em array
    imgArray = np.asarray(img)

    for i in range(len(imgArray)):
        # Transforma a linha em array e inverte
        row = imgArray[i].tolist()
        rowInverted = invertArray(row)
        for j in range(len(rowInverted)):
            newImg.putpixel((j, i), tuple(rowInverted[j]))

    # Salva a imagem
    newImg.save("imagemInvertida.png")
    newImg.show()

except IOError:
    print("Erro ao carregar a imagem")
    exit(1)
