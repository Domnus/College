import Compra
import Pessoa
import Mensagem

if __name__ == "__main__":
	cliente = Pessoa("Rodrigo Faro", "rodrigofaro@record.com", "123456789", "11 99999-9999", 30)
	compra = Compra(cliente, "01/01/2019", 100)

	compra.pagar()

	if compra.getAprovado():
		print("Compra aprovada")
		if cliente.getCNPJ() == None:
			mensagem = Mensagem("EMAIL", banco.nome(), cliente.getNome(), compra.getData(), compra.getValor())

			if mensagem.enviar():
				print("Uma mensagem foi enviada para o seu email")

			else:
				print("Ocorreu um erro ao enviar a mensagem")
		else:
			mensagem = Mensagem("SM", banco.nome(), cliente.getNome(), compra.getData(), compra.getValor())
			if mensagem.enviar():
				print("Uma mensagem foi enviada para o seu SM")

			else:
				print("Ocorreu um erro ao enviar a mensagem")
	else:
		print("Compra não aprovada")
