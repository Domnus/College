#!/usr/bin/env python3

from PIL import Image
import numpy as np

image = Image.open('img.jpg')
image.show()
arr = np.array(image)
novamatriz = []
for i in arr: 
    novoArr = []  
    for j in i: 
        novo = []  
        for a in j: 
            novo.append(a) 
        novoArr.insert(0,novo) 
    novamatriz.append(novoArr)
novoa = np.array(novamatriz)
imagemnova = Image.fromarray(novoa)
imagemnova.show()
