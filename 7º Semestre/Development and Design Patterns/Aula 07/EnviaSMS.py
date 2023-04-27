from AcaoAposNotaFiscal import AcaoAposNotaFiscal

class EnviaSMS(AcaoAposNotaFiscal):
	def Executa(self, nota_fiscal):
		print("Enviando nota por SMS...")