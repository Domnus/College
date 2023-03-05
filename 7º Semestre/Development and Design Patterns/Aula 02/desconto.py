#!/usr/bin/env python3

from abc import ABC, abstractmethod

class CalculaDesconto(ABC):
    @abstractmethod
    def calcula(self, orcamento):
        pass


class DescontoPorCincoItens(CalculaDesconto):
    proximo_desconto = None

    def calcula(self, orcamento):
        if len(orcamento.itens) > 5:
            return orcamento.valor * 0.1
        else:
            return self.proximo_desconto.calcula(orcamento)


class DescontoPorMaisDeQuinhentosReais(CalculaDesconto):
    proximo_desconto = None

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.proximo_desconto.calcula(orcamento)


class SemDesconto(CalculaDesconto):
    def calcula(self, orcamento):
        return 0
        

class Item:
    def __init__(self, valor, nome):
        self.valor = valor
        self.nome = nome


class Orcamento:
    def __init__(self, valor):
        self.valor = valor
        self.itens = []
        self.total = 0

    def getValor(self):
        return self.valor


    def adiciona_item(self, item):
        self.itens.append(item)


orcamento = Orcamento(500)
orcamento.adiciona_item(Item(100, "Item 1"))
orcamento.adiciona_item(Item(100, "Item 2"))
orcamento.adiciona_item(Item(100, "Item 3"))
orcamento.adiciona_item(Item(100, "Item 4"))
orcamento.adiciona_item(Item(100, "Item 5"))
orcamento.adiciona_item(Item(100, "Item 6"))

d1 = DescontoPorCincoItens()
d2 = DescontoPorMaisDeQuinhentosReais()

d1.proximo_desconto = d2
d2.proximo_desconto = SemDesconto()

print(d1.calcula(orcamento))