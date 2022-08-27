from Emissor.EmissorCriador import EmissorCriador

class Maquininha:
    def __init__(self, cartao, valorCompra, senha):
        self.cartao = cartao,
        self.valorCompra = valorCompra
        self.senha = senha

    def validar(self):
        emissorCriador = EmissorCriador(self.cartao, self.valorCompra, self.senha)
        emissor = emissorCriador.criar()

        emissor.enviar(self.cartao, self.valorCompra, self.senha)
    