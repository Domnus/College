class Processo:
	def __init__(self, id, tempo_entrada, tempo_execucao, prioridade = 1):
		self.id = id
		self.tempo_entrada = tempo_entrada
		self.tempo_execucao = tempo_execucao
		self.prioridade = prioridade
