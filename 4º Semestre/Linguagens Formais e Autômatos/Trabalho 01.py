table = []
alfabeto = []
estados = []
estadosFinais = []
inicial = '' 
final = []
height = 0 
length = 0
 
def validarPalavra(palavra):
	estadoAtual = inicial	

	for letter in palavra:
		if letter not in alfabeto:
			return False

	print(estadoAtual)
	for letter in palavra:
		for index, item in enumerate(table):
			if estadoAtual == item[0]:
				local = table[0].index(letter)
				if letter == table[0][local]:
					estadoAtual = item[local]
					break
		print(estadoAtual)


def showTable(table, location = []):
	for estados in table:
		for estado in estados:
			if len(location) > 0:
				if table.index(estados) == location[0] and estados.index(estado) == location[1]:
					print('|????|', end=" ")
					location = []
					continue
			if estado in estadosFinais:
				print('|{:^4}|'.format("*"+estado), end=" ")
			else:
				print('|{:^4}|'.format(estado), end=" ")
		print("")


def createTable(height, length, estadosFinais):
	for i in range(height):
		table.append([])
		for j in range(length):
			table[i].append([])

	for i in range(height):
		for j in range(length):
			table[i][j] = ''


	table[0][0] = 'δ'

	for i in range(length - 1):
		table[0][i+1] = alfabeto[i]

	for i in range(height - 1):
		table[i + 1][0] = estados[i]
	return table


def readTable():
	location = []

	print("Digite os valores da tabela: [Enter para estado nulo] \n")
	for i in range(1, height):
		for j in range(1, length):
			location = [i, j]
			showTable(table, location)	
			while True:
				letra = input("-> ")	
				if letra in (estados):
					if letra == '':
						letra = '∅'
					table[i][j] = letra
					break
				else:
					print("Alfabeto inválido!!!")
					continue
	location = []
	showTable(table, location)	

def init():
	global height
	global length
	global alfabeto
	global estados
	global inicial
	global estadosFinais
	alfabeto = input("Digite o alfabeto do autômato separado por um espaço: ").split() 
	estados  = input("Digite o nome dos estados do autômato separados por um espaço: ").split()
	estados.append('')

	while True:
		inicial = input("Digite o estado inicial: ")
		if inicial in estados:
			while True:
				cont = 0
				estadosFinais = input("Digite o(s) estado(s) final(is) separados por um espaço: ").split()
				for estado in estadosFinais:
					if estado in estados:
						cont += 1
				if cont == len(estadosFinais):
					break
				else:
					print("Algum estado está incorreto!!!")
			break
		else:
			print("Estado inválido!!!")


	height = len(estados) 
	length = len(alfabeto) + 1

	table = createTable(height, length, estadosFinais)

	readTable()


def createMachine(automatoCriado):
	if automatoCriado:
		op = input("Já existe um autômato criado. Deseja substituí-lo? [S/N] ").upper()[0]
		if op == "S":
			init()
			return True
		else:
			print("Voltando ao menu principal")
			return False
	else:
		init()
		return True

def menu(): 
	automatoCriado = True
	while True:
		print ("1 - Criar autômato ")
		print ("2 - Validar palavra ")	
		print ("3 - Sair ")	
		resposta = input("Escolha uma opção: ")
		if resposta == '1':
			automatoCriado = createMachine(automatoCriado)
		elif resposta == '2':
			if automatoCriado == False:
				op = input("Nenhum autômato foi criado. Deseja criar um agora? [S/N] ").upper()[0]
				if op == "S":
					automatoCriado = createMachine(automatoCriado)
				else:
					print("Voltando ao menu principal")
			else:
				showTable(table)
				validarPalavra(input("Digite a palavra a ser validada pelo autômato acima -> "))
		elif resposta == '3':
			break
		else:
			print("Opção incorreta.")


menu()
