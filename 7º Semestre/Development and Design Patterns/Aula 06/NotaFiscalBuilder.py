from NotaFiscal import NotaFiscal

class NotaFiscalBuilder(object):
	def __init__(self):
		self.__razao_social = None
		self.__cnpj = None
		self.__itens = []
		self.__detalhes = None
		self.__data_de_emissao = None
		self.__observacoes = None
		self.__valor_bruto = 0
		self.__impostos = 0

	def com_razao_social(self, razao_social):
		self.__razao_social = razao_social
		return self

	def com_cnpj(self, cnpj):
		self.__cnpj = cnpj
		return self

	def com_itens(self, item):
		self.__itens.append(item)
		self.__valor_bruto += item.valor
		self.__impostos = self.__valor_bruto * 0.05

		return self

	def com_detalhes(self, detalhes):
		self.__detalhes = detalhes
		return self

	def com_data_de_emissao(self, data_de_emissao):
		self.__data_de_emissao = data_de_emissao
		return self

	def com_observacoes(self, observacoes):
		self.__observacoes = observacoes
		return self

	def constroi(self):
		if self.__razao_social is None:
			raise Exception('Razão social deve ser preenchida')

		if self.__cnpj is None:
			raise Exception('CNPJ deve ser preenchido')

		if self.__itens is None:
			raise Exception('Itens deve ser preenchido')

		return NotaFiscal(self.__razao_social, self.__cnpj, self.__itens, self.__detalhes, self.__data_de_emissao, self.__observacoes, self.__valor_bruto, self.__impostos)