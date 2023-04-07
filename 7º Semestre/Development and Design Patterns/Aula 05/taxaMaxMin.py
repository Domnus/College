#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Item:
    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor = valor

    def getNome(self) -> str:
        return self.nome

    def getValor(self) -> float:
        return self.valor


class Orcamento:
    def __init__(self, valor: float):
        self.valor = valor
        self.itens = []

    def getValor(self) -> float:
        return self.valor

    def getItens(self) -> list:
        return self.itens

    def getNomeItens(self) -> list:
        nomes = []
        for item in self.itens:
            nomes.append(item.getNome())
        return nomes
    
    def addItem(self, item: Item):
        self.itens.append(item)


class Imposto(ABC):
    @abstractmethod
    def calcula(self, orcamento: Orcamento) -> float:
        pass


class ImpostoTemplate(Imposto):
    def calcula(self, orcamento: Orcamento) -> float:
        if self.UsaTaxaMaxima(orcamento):
            return self.taxaMaxima(orcamento)
        else:
            return self.taxaMinima(orcamento)
    
    @abstractmethod
    def UsaTaxaMaxima(self, orcamento: Orcamento) -> bool:
        pass

    @abstractmethod
    def taxaMaxima(self, orcamento: Orcamento) -> float:
        pass

    @abstractmethod
    def taxaMinima(self, orcamento: Orcamento) -> float:
        pass


class IHIT(ImpostoTemplate):
    def UsaTaxaMaxima(self, orcamento: Orcamento) -> bool:
        nomeItens = orcamento.getNomeItens()
        for nome in nomeItens:
            if nomeItens.count(nome) > 1:
                return True
        return False

    def taxaMaxima(self, orcamento: Orcamento) -> float:
        return orcamento.getValor() * 0.13 + 100

    def taxaMinima(self, orcamento: Orcamento) -> float:
        return orcamento.getValor() * (0.01 * len(orcamento.getItens()))


ihit = IHIT()
orcamento = Orcamento(500)
orcamento.addItem(Item("CANETA", 250))
# orcamento.addItem(Item("CANETA", 250))
orcamento.addItem(Item("LAPIS", 250))
orcamento.addItem(Item("BORRACHA", 250))
print(ihit.calcula(orcamento))