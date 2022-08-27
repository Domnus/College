class Cartao:
	def __init__(self, nome, numero, bandeira, senha, saldo):
		self.nome = nome
		self.numero = numero
		self.__bandeira = bandeira
		self.senha = senha
		self.saldo = saldo

	def getNome(self):
		return self.nome

	def getNumero(self):
		return self.numero

	def getBandeira(self):
		return self.__bandeira
