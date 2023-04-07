# Bento Carlos Silva dos Santos RA: 600784
# Hugo Seiti Odajima            RA: 606537
# Paulo Guilherme Astrauskas    RA: 548111

from math import sin, cos, radians
from tabulate import tabulate

import numpy as np

Cx = 2
Cy = 2
Cz = 2

translacao = \
[
    [1,   0,  0, Cx],
    [0,   1,  0, Cy],
	[0,   0,  1, Cz],
    [0,   0,  0,  1]
]

Sx = 2
Sy = 2
Sz = 2

escala = \
[
    [Sx,  0,  0, 0],
    [ 0, Sy,  0, 0],
	[ 0,  0, Sz, 0],
    [ 0,  0,  0, 1]
]

Rx = 45
rotacaoX = \
[
	[1, 0, 0, 0],
	[0, cos(radians(Rx)), -sin(radians(Rx)), 0],
	[0, sin(radians(Rx)), cos(radians(Rx)), 0],
	[0, 0, 0, 1]
]

Ry = 45
rotacaoY = \
[
	[cos(radians(Ry)), 0, sin(radians(Ry)), 0],
	[0, 1, 0, 0],
	[-sin(radians(Ry)), 0, cos(radians(Ry)), 0],
	[0, 0, 0, 1]	
]

Rz = -45
rotacaoZ = \
[
	[cos(radians(Rz)), -sin(radians(Rz)), 0, 0],
	[sin(radians(Rz)), cos(radians(Rz)), 0, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 1]
]

operacoes = [translacao, escala, rotacaoX, rotacaoY, rotacaoZ]

def multiplicaOperacoes(operacoes):
	matriz = np.identity(4)
	for operacao in operacoes:
		matriz = np.dot(matriz, operacao)
	return matriz


pontosCubo3D = \
[
	[1, 2, 1, 1], #H
	[1, 2, 2, 1], #G
	[2, 2, 1, 1], #E
	[2, 2, 2, 1], #F
	[1, 1, 1, 1], #D
	[1, 1, 2, 1], #C
	[2, 1, 1, 1], #A
	[2, 1, 2, 1]  #B
]

matrizMultiplicadora = multiplicaOperacoes(operacoes)

headers = ['', '', '', '']

pontosCubo3DTransformados = []

for ponto in pontosCubo3D:
	pontoTransformado = np.dot(matrizMultiplicadora, ponto)
	pontosCubo3DTransformados.append(pontoTransformado)

print(tabulate(pontosCubo3DTransformados, headers=headers, floatfmt=".2f"))