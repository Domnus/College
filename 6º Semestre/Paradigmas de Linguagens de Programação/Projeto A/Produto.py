class Produto():
	def __init__(self, altura, largura, comprimento, peso):
		self.altura = altura
		self.largura = largura
		self.comprimento = comprimento
		self.peso = peso
		
	def getCubicoIndividual(self):
		return self.altura * self.largura * self.comprimento

	def getCubicoComFator(self):
		return self.getCubicoIndividual() / 6

