class em_aprovacao():
    Status = 'Em aprovação'

    def aplica_desconto_extra(self, orcamento):
        orcamento.valor -= orcamento.valor * 0.05
    
    def aprova(self):
        return aprovado()

    def reprova(self):
        return reprovado()
    
    def finaliza(self):
        raise Exception('Orçamento em aprovação não pode ser finalizado')

    def getStatus(self):
        return self.Status

class aprovado():
    Status = 'aprovado'

    def aplica_desconto_extra(self, orcamento):
        orcamento.valor -= orcamento.valor * 0.02
    
    def aprova(self):
        raise Exception('Orçamento já está em estado de aprovação')
    
    def reprova(self):
        raise Exception('Orçamento aprovado não pode ser reprovado')

    def finaliza(self):
        return finalizado()
    
    def getStatus(self):
        return self.Status


class reprovado():
    Status = 'repovado'

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

    def aprova(self):
        raise Exception('Orçamento reprovado não pode ser aprovado')

    def reprova(self):
        raise Exception('Orçamento já está reprovado')

    def finaliza(self):
        return finalizado()
    
    def getStatus(self):
        return self.Status

class finalizado():
    Status = 'finalizado'

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra')

    def aprova(self):
        raise Exception('Orçamento finalizado não pode ser aprovado')

    def reprova(self):
        raise Exception('Orçamento finalizado não pode ser reprovado')

    def finaliza(self):
        raise Exception('Orçamento já está finalizado')
    
    def getStatus(self):
        return self.Status

class orcamento():
    def __init__(self, valor):
        self.valor = valor
        self.estado_atual = em_aprovacao()

    def aplicar_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def aprova(self):
        self.estado_atual = self.estado_atual.aprova()

    def reprova(self):
        self.estado_atual = self.estado_atual.reprova()

    def finaliza(self):
        self.estado_atual = self.estado_atual.finaliza()
    
def menu():
    print('1 - Aprovar')
    print('2 - Reprovar')
    print('3 - Finalizar')
    print('4 - Aplicar desconto extra')
    print('0 - Sair')
    return int(input('Escolha uma opção: '))

def main():
	valorzao = orcamento(500)
	while True:
		print('Status atual: {}'.format(valorzao.estado_atual.getStatus()))
		print('valor: {}'.format(valorzao.valor))	
		opcao = menu()
		if opcao == 1:
			valorzao.aprova()
		elif opcao == 2:
			valorzao.reprova()
		elif opcao == 3:
			valorzao.finaliza()
		elif opcao == 4:
			valorzao.aplicar_desconto_extra()
		elif opcao == 0:
			break
		else:
			print('Opção inválida')
main()