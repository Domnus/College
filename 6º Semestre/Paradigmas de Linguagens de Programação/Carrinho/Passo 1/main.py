#Andressa Caroline Reis Bueno 	RA: 607290
#Bento Carlos Silva dos Santos RA: 600784
#Frederico Hanai 				RA: 604593

class Item():
	def __init__(self, id, produto, preco):
		self.id = id
		self.produto = produto
		self.preco = preco

	def getPreco(self):
		return self.preco


class Carrinho():
	def __init__(self):
		self.itens = []
		self.total = 0  # type: ignore

	def adicionar(self, item):
		self.itens.append(item)
		self.total += item.preco

	def remover(self, item):
		self.itens.remove(item)
		self.total -= item.preco

	def total(self):
		return sum(self.itens.getPreco())


carrinho = Carrinho()
carrinho.adicionar(Item(1, 'Iphone', 499))
carrinho.adicionar(Item(2, 'Kindle', 179))
carrinho.adicionar(Item(3, 'Macbook Pro', 1199))
print(f"O total do carrinho é: R${carrinho.total}")
