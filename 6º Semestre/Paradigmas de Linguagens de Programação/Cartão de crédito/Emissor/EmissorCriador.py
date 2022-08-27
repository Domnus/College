from Cartao import Cartao
from Emissor.EmissorVISA import EmissorVISA
from Emissor.EmissorMASTERCARD import EmissorMASTERCARD

class EmissorCriador():

    def __init__(self, cartao: Cartao, valorCompra: int, senha: int):
        self.cartao = cartao
        self.valorCompra = valorCompra
        self.senha = senha

    def criar(self):
        bandeira = self.cartao[0].getBandeira()
        if bandeira == "VISA":
            return EmissorVISA(self.cartao, self.valorCompra, self.senha)
        elif bandeira == "MASTERCARD":
            return EmissorMASTERCARD(self.cartao, self.valorCompra, self.senha)
        else:
            print("Bandeira inválida!")
