from Emissor.Emissor import Emissor

class EmissorVISA(Emissor):

    def enviar(self, cartao, valorCompra, senha):
        print("Pagamento aprovado!")