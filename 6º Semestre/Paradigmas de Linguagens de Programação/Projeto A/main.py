# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos               RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Guilherme Astrauskas RA: 548111

from Produto import Produto

produtos = [
	[35, 8, 38, 3000],
	[35, 8, 38, 3000],
	[18, 8, 17, 188]
]

produtosOrdenados = []

for produto in produtos:
	produto.sort()
	produtosOrdenados.append(Produto(produto[0], produto[1], produto[2], produto[3]))


def empilhamento_soma(): # B1513
	 return(sum(map(lambda produto: produto[0], produtos)))


def empilhamento_maior(campo): # C1513 | D1513
	return(max(map(lambda produto: getattr(produto, campo), produtosOrdenados)))


def peso_total():
	return sum(map(lambda produto: produto.peso, produtosOrdenados))


def correcao(valor, correcao):
	if valor > correcao:
		return valor
	return correcao


def correcao_minimas(dimensao): # B1514 | C1514 | D1514
	match (dimensao):
		case "altura":
			correcaoMinimas = empilhamento_soma()
			return correcao(correcaoMinimas, 2)
		case "largura":
			correcaoMinimas = empilhamento_maior(1)
			return correcao(correcaoMinimas, 11)
		case "comprimento":
			correcaoMinimas = empilhamento_maior(2)
			return correcao(correcaoMinimas, 16)


def soma_cubico(tipo):
	match(tipo):
		case "individual": # H1512
			return sum(map(lambda produto: produto.getCubicoIndividual(), produtosOrdenados))
		case "comFator": # I1512
			return round(sum(map(lambda produto: produto.getCubicoComFator(), produtosOrdenados)))

	
def dimensao_alternativa_raiz_cubica(): # B1516 | C1516 | D1516
	return round(soma_cubico("individual") ** (1/3), 1) # type: ignore
	

def raiz_cubica_maximas(dimensao): # B1518 | C1518 | D1518
	match (dimensao):
		case "altura":
			if dimensao_alternativa_raiz_cubica() < empilhamento_maior("comprimento"): 
				return empilhamento_maior("comprimento")
			else:
				return dimensao_alternativa_raiz_cubica()
		case "largura":
			if dimensao_alternativa_raiz_cubica() < empilhamento_maior("largura"): 
				return empilhamento_maior("largura")
			else:
				return dimensao_alternativa_raiz_cubica()
		case "comprimento":
			return round((soma_cubico("individual") / raiz_cubica_maximas("altura")) / raiz_cubica_maximas("largura"), 1) # type: ignore


def check_count_35(valor):
	return 0 if valor == 35 else 1
	

def count_35(dimensao):
	return sum(map(lambda produto: check_count_35(getattr(produto, dimensao)), produtosOrdenados))


def check_somatoria_35(dimensao):
	return map(lambda produto: 0 if check_count_35(getattr(produto, dimensao)) == 0 else check_count_35(getattr(produto, dimensao)), produtosOrdenados)


def somatoria_35(dimensao):
	return sum(check_somatoria_35(dimensao))

			
def aux_tratamento_min_maior(dimensao):
	if dimensao_alternativa_raiz_cubica() < empilhamento_maior(dimensao):
		return empilhamento_maior(dimensao)
	else:
		return dimensao_alternativa_raiz_cubica()


def tratamento_min_maior(dimensao): # B1528
	match (dimensao):
		case "altura":
			if count_35(dimensao) > 0: # type: ignore
				return count_35(dimensao)
			else:
				return aux_tratamento_min_maior("comprimento")	
		case "largura":
			return aux_tratamento_min_maior(dimensao)
		case "comprimento":
			return round((soma_cubico("individual") / tratamento_min_maior("altura")) / tratamento_min_maior("largura"), 1) # type: ignore


def arredondar_cima(dimensao):
	match (dimensao):
		case "altura":
			return round(tratamento_min_maior(dimensao), 1) # type: ignore
		case "largura":
			return round(tratamento_min_maior(dimensao), 1) # type: ignore
		case "comprimento":
			return round(tratamento_min_maior(dimensao), 1) # type: ignore


def frete_facil():
	return sorted((arredondar_cima("altura"), arredondar_cima("largura"), arredondar_cima("comprimento"))) # type: ignore
	

def correcao_min(dimensao):
	match(dimensao):
		case "altura":
			return 2 if frete_facil()[0] < 2 else frete_facil()[0]
		case "largura":
			return 11 if frete_facil()[1] < 11 else frete_facil()[1]
		case "comprimento":
			return 16 if frete_facil()[2] < 16 else frete_facil()[2]
	

def peso_cubico():
	return round((correcao_min("altura") * correcao_min("largura") * correcao_min("comprimento")) / 6) # type: ignore


def peso_tarifado():
	return peso_cubico() if peso_cubico() > 4999 else peso_total()


def printAllFunctions():
	print("Peso Total: ", peso_total())
	print("Peso Cubico: ", peso_cubico())
	print("Peso Tarifado: ", peso_tarifado())
	print("Dimensao Alternativa Raiz Cubica: ", dimensao_alternativa_raiz_cubica())
	print("Raiz Cubica Maximas Altura: ", raiz_cubica_maximas("altura"))
	print("Raiz Cubica Maximas Largura: ", raiz_cubica_maximas("largura"))
	print("Raiz Cubica Maximas Comprimento: ", raiz_cubica_maximas("comprimento"))
	print("Empilhamento Soma: ", empilhamento_soma())
	print("Empilhamento Maior Altura: ", empilhamento_maior("altura"))
	print("Empilhamento Maior Largura: ", empilhamento_maior("largura"))
	print("Empilhamento Maior Comprimento: ", empilhamento_maior("comprimento"))
	print("Correcao Minimas Altura: ", correcao_min("altura"))
	print("Correcao Minimas Largura: ", correcao_min("largura"))
	print("Correcao Minimas Comprimento: ", correcao_min("comprimento"))
	print("Soma Cubico Individual: ", soma_cubico("individual"))
	print("Soma Cubico Com Fator: ", soma_cubico("comFator"))
	print("Dimensao Alternativa Raiz Cubica: ", dimensao_alternativa_raiz_cubica())
	print("Raiz Cubica Maximas Altura: ", raiz_cubica_maximas("altura"))
	print("Raiz Cubica Maximas Largura: ", raiz_cubica_maximas("largura"))
	print("Raiz Cubica Maximas Comprimento: ", raiz_cubica_maximas("comprimento"))
	print("Count 35 Altura: ", count_35("altura"))
	print("Count 35 Largura: ", count_35("largura"))
	print("Count 35 Comprimento: ", count_35("comprimento"))
	print("Somatoria 35 Altura: ", somatoria_35("altura"))
	print("Somatoria 35 Largura: ", somatoria_35("largura"))


printAllFunctions()