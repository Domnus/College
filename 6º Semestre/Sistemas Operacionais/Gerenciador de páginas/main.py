# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Astrauskas 		 	 RA: 548111

from Pagina import Pagina
from random import randint

tabelaPaginas = {}

memoria = []

for i in range(4):
	memoria.append([])
	for j in range(4):
		memoria[i].append([])
		memoria[i][j] = 0

def menor(x, y):
	if int(x, 2) < int(y, 2):
		return x
	return y

while True:
	num = randint(5, 8)
	idPagina = 0

	for i in range(num):
		tabelaPaginas[idPagina] = Pagina(idPagina, 0, None)
		idPagina += 1

	for i in range(idPagina):
		print(tabelaPaginas[i].id, tabelaPaginas[i].referencia, tabelaPaginas[i].moldura)


	while True:
		for i in range(idPagina):
			print(tabelaPaginas[i].id, tabelaPaginas[i].referencia, tabelaPaginas[i].moldura)

		res = input("Digite o id da pagina que deseja acessar: ")
		if res.isnumeric():
			pagID = int(res)

			if pagID in range(idPagina):
				print("Pagina existe")
				molduras = []
				realocado = False

				for i in range(len(memoria)):
					linha = ''
					for j in range(len(memoria[i])):
						linha += str(memoria[i][j])
					molduras.append([linha, i])

				molduras.sort(key=lambda pagina: int(pagina[0], 2))
				linhaVazia = molduras[0][1]

				referencia = tabelaPaginas[pagID].referencia

				if referencia == 1:
					linhaVazia = tabelaPaginas[pagID].moldura
					realocado = True

				for i in range(len(memoria)):
					for j in range(len(memoria[i])):
						if i == linhaVazia:
							memoria[i][j] = 1

				for i in range(len(memoria)):
					for j in range(len(memoria[i])):
						if i == linhaVazia:
							memoria[j][i] = 0

				tabelaPaginas[pagID].referencia = 1

				for id in range(idPagina):
					moldura = tabelaPaginas[id].moldura
					if moldura != None and moldura == linhaVazia:
						tabelaPaginas[id].moldura = None
						if not realocado:
							tabelaPaginas[id].referencia = 0

				tabelaPaginas[pagID].moldura = linhaVazia

				for i in range(len(memoria)):
					for j in range(len(memoria[i])):
						print(memoria[i][j], end=" ")

					print()

			else:
				print("Pagina não existe")
		else:
			print("Número inválido")