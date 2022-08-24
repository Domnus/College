class Pessoa:
	def __init__(self, nome, email, cpf, telefone, idade, cnpj = None, cartao = None):
		self.nome = nome
		self.idade = idade
		self.email = email
		self.cpf = cpf
		self.cnpj = cnpj
		self.telefone = telefone
		self.cartao = cartao
	
	def getCNPJ(self):
		return self.cnpj
