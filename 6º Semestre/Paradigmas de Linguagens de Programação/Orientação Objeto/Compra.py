class Compra:
	def __init__(self, Pessoa, data, valor, aprovado = None):
		self.Pessoa = Pessoa
		self.data = data
		self.valor = valor
		self.aprovado = aprovado

	def setAprovado(self):
		self.aprovado = True

	def getAprovado(self):
		return self.aprovado

	def getData(self):
		return self.data

	async def pagar(self):
		resposta = await banco.pagar(self)
		if resposta:
			self.aprovado = True
		else:
			self.aprovado = False