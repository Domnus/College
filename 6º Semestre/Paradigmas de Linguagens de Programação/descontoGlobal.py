## Bento Carlos Silva dos Santos RA: 600784
## Hugo Seiti Odajima RA: 606537

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
	def __init__(self):
		self.itens = []
		self.valor = 0
		self.desconto = 0

	def setDesconto(self, desconto):
		self.desconto = desconto

	def getDesconto(self):
		return self.desconto

	def getItens(self):
		return self.itens

	def addItem(self, item):
		self.itens.append(item)

	def removeItem(self, item):
		self.itens.remove(item)

	def getValor(self):
		return self.valor

	def calculaValor(self):
		valor = 0
		for item in self.itens:
			valor += item.getPreco() - (item.getPreco() * (self.desconto / 100)) * item.getQuantidade()

		self.valor = valor;

	def setValor(self, valor):
		self.valor = valor

carrinho = Carrinho()
carrinho.setDesconto(10)

cliente = Cliente("Rodrigo Faro", 1001)

carrinho.addItem(Item("Celular", 1000, 1))
carrinho.addItem(Item("Notebook", 2000, 1))
carrinho.addItem(Item("Tablet", 500, 1))
carrinho.addItem(Item("Mouse", 100, 1))
carrinho.addItem(Item("Teclado", 200, 1))
carrinho.addItem(Item("Monitor", 500, 1))
carrinho.addItem(Item("Impressora", 1000, 1))

carrinho.calculaValor()

if cliente.getPontos() > 1000:
	carrinho.setValor(carrinho.getValor() - (carrinho.getValor() * 0.05))

print(f"O valor do carrinho é R${carrinho.getValor()}")