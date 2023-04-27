from AcaoAposNotaFiscal import AcaoAposNotaFiscal

class EnviaEmail(AcaoAposNotaFiscal):
	def Executa(self, nota_fiscal):
		print("Enviando nota por e-mail...")