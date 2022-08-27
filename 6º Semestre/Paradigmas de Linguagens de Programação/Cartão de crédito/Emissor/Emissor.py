from abc import ABC, abstractmethod
from Cartao import Cartao

class Emissor(ABC):

    def __init__(self, cartao: Cartao, valorCompra: int, senha: int):
        self.cartao = cartao
        self.valorCompra = valorCompra
        self.senha = senha

    @abstractmethod
    def enviar(self, cartao, valorCompra, senha):
        self
