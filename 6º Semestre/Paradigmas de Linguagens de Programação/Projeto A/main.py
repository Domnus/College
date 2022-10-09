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

def empilhamento_soma():
	 return(sum(map(lambda produto: produto[0], produtos)))

def empilhamento_maior(campo):
	return(max(map(lambda produto: produto[campo], produtos)))


def correcao_empilhamento(dimensao):
	match (dimensao):
		case "altura":
			correcaoMinimas = empilhamento_soma()
		case "largura":
			correcaoMinimas = empilhamento_maior(1)
		case "comprimento":
			correcaoMinimas = empilhamento_maior(2)

	return correcaoMinimas if (correcaoMinimas > 2) else 2

print(correcao_empilhamento("altura"))
print(correcao_empilhamento("largura"))
print(correcao_empilhamento("comprimento"))