class NotaFiscal(object):
	def __init__(self, razao_social, cnpj, itens, detalhes, data_de_emissao, observacoes, valor_bruto, impostos):
		self.razao_social = razao_social
		self.cnpj = cnpj
		self.itens = itens
		self.detalhes = detalhes
		self.data_de_emissao = data_de_emissao
		self.observacoes = observacoes
		self.valor_bruto = valor_bruto
		self.impostos = impostos