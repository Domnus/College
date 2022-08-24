def Mensagem():
	def __init__(self, formato, remetente, destinatario, assunto, texto):
		self.formato = formato
		self.remetente = remetente
		self.destinatario = destinatario
		self.assunto = assunto
		self.texto = texto
	
	async def enviarMensagem(self):
		match(self.formato):
			case "SMS":
				res = await sendSMS(self.remetente, self.destinatario, self.assunto, self.texto)
			case "EMAIL":
				res = await sendEmail(self.remetente, self.destinatario, self.assunto, self.texto)
			case "SM":
				res = await sendSM(self.remetente, self.destinatario, self.assunto, self.texto)
			case other:
				print("Formato de mensagem inválido")

		if res:
			return True
		else:
			return False
		