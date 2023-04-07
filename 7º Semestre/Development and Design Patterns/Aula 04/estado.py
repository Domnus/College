from abc import ABC, abstractmethod

def clear():
	import os
	os.system('cls' if os.name=='nt' else 'clear')

class Estado(ABC):
	@abstractmethod
	def aplica_desconto_extra(self, orcamento):
		pass

	@abstractmethod
	def aprova(self):
		pass

	@abstractmethod
	def reprova(self):
		pass

	@abstractmethod
	def finaliza(self):
		pass

	@abstractmethod
	def getNomeEstado(self):
		pass

class Em_Aprovacao(Estado):
	estadoNome = "Em aprovação"

	def aplica_desconto_extra(self, orcamento):
		orcamento.valor -= orcamento.valor * 0.05

	def aprova(self):
		return Aprovado()

	def reprova(self):
		return Reprovado()

	def finaliza(self):
		raise Exception("Orçamento em aprovação não pode ir para finalizado!")

	def getNomeEstado(self):
		return self.estadoNome


class Aprovado(Estado):
	estadoNome = "Aprovado"
	
	def aplica_desconto_extra(self, orcamento):
		orcamento.valor -= orcamento.valor * 0.02

	def aprova(self):
		raise Exception("Orçamento já está aprovado!")

	def reprova(self):
		raise Exception("Orçamento já está aprovado!")
	
	def finaliza(self):
		return Finalizado()

	def getNomeEstado(self):
		return self.estadoNome

		
class Reprovado(Estado):
	estadoNome = "Reprovado"

	def aplica_desconto_extra(self, orcamento):
		print("Orçamentos reprovados não recebem desconto extra!")

	def aprova(self):
		raise Exception("Orçamento já está reprovado!")
	
	def reprova(self):
		raise Exception("Orçamento já está reprovado!")
	
	def finaliza(self):
		return Finalizado()

	def getNomeEstado(self):
		return self.estadoNome


class Finalizado(Estado):
	estadoNome = "Finalizado"

	def aplica_desconto_extra(self, orcamento):
		raise Exception("Orçamento já está finalizado!")

	def aprova(self):
		raise Exception("Orçamento já está finalizado!")
	
	def reprova(self):
		raise Exception("Orçamento já está finalizado!")
	
	def finaliza(self):
		raise Exception("Orçamento já está finalizado!")

	def getNomeEstado(self):
		return self.estadoNome


class Orcamento(object):
	def __init__(self, valor):
		self.valor = valor
		self.estado_atual = Em_Aprovacao()

	def aplica_desconto_extra(self):
		self.estado_atual.aplica_desconto_extra(self)

	def aprova(self):
		self.estado_atual = self.estado_atual.aprova()

	def reprova(self):
		self.estado_atual = self.estado_atual.reprova()

	def finaliza(self):
		self.estado_atual = self.estado_atual.finaliza() 


def menu():
	print("1 - Aprovar")
	print("2 - Reprovar")
	print("3 - Finalizar")
	print("4 - Aplicar desconto extra")
	print("5 - Sair")
	return int(input("Escolha uma opção: "))


def main():
	orcamento = Orcamento(1000)
	while True:
		clear()
		print(f"Estado atual do orçamento: {orcamento.estado_atual.getNomeEstado()}")
		print(f"Valor atual: {orcamento.valor}\n")
		opcao = menu()
		if opcao == 1:
			orcamento.aprova()
		elif opcao == 2:
			orcamento.reprova()
		elif opcao == 3:
			orcamento.finaliza()
		elif opcao == 4:
			orcamento.aplica_desconto_extra()
		elif opcao == 5:
			break
		else:
			print("Opção inválida!")

main()