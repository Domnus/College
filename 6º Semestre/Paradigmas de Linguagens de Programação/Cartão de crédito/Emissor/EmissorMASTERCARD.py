from Emissor.Emissor import Emissor

class EmissorMASTERCARD(Emissor):

    def enviar(self, cartao, valorCompra, senha):
        print("Pagamento aprovado!")