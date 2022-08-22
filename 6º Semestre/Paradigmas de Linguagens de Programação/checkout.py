## Bento Carlos Silva dos Santos RA: 600784
## Hugo Seiti Odajima RA: 606537

# Declarativo

def calculaDesconto(cliente, preco):
	if cliente.pontos > 1000:
		return aplicaDesconto(preco, 0.05)

	return preco

calculaDesconto(cliente, carrinho.getPreco())


# Imperativo

class Cliente:
	def __init__(self, nome, pontos):
		self.nome = nome
		self.pontos = pontos

	def getNome(self):
		return self.nome
	
	def getPontos(self):
		return self.pontos


class Item:
	def __init__(self, nome, preco, quantidade):
		self.nome = nome
		self.preco = preco
		self.quantidade = quantidade

	def getNome(self):
		return self.nome
	
	def getPreco(self):
		return self.preco

	def getQuantidade(self):
		return self.quantidade


class Carrinho:
	def __init__(self, itens, valor):
		self.itens = itens
		self.valor = valor

	def getItens(self):
		return self.itens

	def addItem(self, item):
		self.itens.append(item)

	def removeItem(self, item):
		self.itens.remove(item)

	def getValor(self):
		for item in self.itens:
			self.valor += item.getPreco() * item.getQuantidade()

	def setValor(self, valor):
		self.valor = valor


cliente = Cliente("Rodrigo Faro", 1000)

itens = []

carrinho = Carrinho(0, itens)

if cliente.getPontos() > 1000:
	Carrinho.setValor = carrinho.getValor() - (carrinho.getValor() * 0.05)
