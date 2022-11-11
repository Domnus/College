# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai			 RA: 604593
# Hugo Seiti Odajima		 RA: 606537
# Paulo Astrauskas			 RA: 548111

from math import ceil

alfabeto = "abcdefghijklmnopqrstuvwxyz"
filler = 'ß'
chave = "MEGABUCK"
len_chave = {}
chaves_ord = sorted(len_chave.keys())
chave_sorted = sorted(chave)

for i in range(len(chave)):
	len_chave[chave_sorted.index(chave[i]) + 1] = chave[i] 

chaves_ord = sorted(len_chave.keys())

def cifrar(mensagem):
	matriz = []
	mensagem_temp = mensagem
	index = 0
	mensagem_cifrada = ''

	while len(mensagem_temp) > 0:
		matriz.append([])
		contador = 0

		if len(mensagem_temp) < len(chave):
			while len(mensagem_temp) < len(chave):
				mensagem_temp += filler

		for i in range(len(chave)):
			if contador < len(chave):
				matriz[index].append(mensagem_temp[contador])
				contador += 1

		mensagem_temp = mensagem_temp[contador:]
		if len(mensagem_temp) == 0:
			break
		index += 1


	for i in range(len(chave)):
		letra_pos = chave.index(len_chave[chaves_ord[i]])
		for j in range(len(matriz)):
			mensagem_cifrada += matriz[j][letra_pos]
	
	return mensagem_cifrada


def decifrar(mensagem):
	matriz = []
	num_linhas = ceil(len(mensagem) / len(chave))
	mensagem_decifrada = ''
	
	for i in range(num_linhas):
		matriz.append([])
		for j in range(len(chave)):
			matriz[i].append([])

	for i in range(len(chave)):
		letra_pos = chave.index(len_chave[chaves_ord[i]])
		for j in range(len(matriz)):
			matriz[j][letra_pos] = mensagem[0]
			mensagem = mensagem[1:]

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] != filler:
				mensagem_decifrada += matriz[i][j]

	return mensagem_decifrada


def main():
	#mensagem = "pleasetransferonemilliondollarstomyswissbankaccountsixtwotwo" 
	mensagem = input("Digite a mensagem: ")
	#mensagemCifrada = "afllsksoselawaiatoossctclnmomantesilyntwrnntsowdpaedobuoeriricxb"
	mensagemCifrada = cifrar(mensagem)
	print("Mensagem cifrada: ", mensagemCifrada)
	mensagemDecifrada = decifrar(mensagemCifrada)
	print("Mensagem decifrada: ", mensagemDecifrada)

main()