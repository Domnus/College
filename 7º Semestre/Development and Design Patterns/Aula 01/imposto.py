#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor


class Imposto(ABC):
    @abstractmethod
    def calcula(self):
        pass


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.getValor() * 0.1


class PIS(Imposto):
    def calcula(self, orcamento):
        return orcamento.getValor() * 0.06


class COFINS(Imposto):
    def calcula(self, orcamento):
        return orcamento.getValor() * 0.01


class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.getValor() * 0.06


class CalculaImposto():
    def realizaCalculo(self, orcamento, imposto):
        return imposto.calcula(orcamento)


orc = Orcamento(500)
icms = ICMS()
pis = PIS()
cofins = COFINS()
iss = ISS()

calcula_imposto = CalculaImposto()
print(f"ICMS:   R${calcula_imposto.realizaCalculo(orc, icms)}")
print(f"PIS:    R${calcula_imposto.realizaCalculo(orc, pis)}")
print(f"COFINS: R${calcula_imposto.realizaCalculo(orc, cofins)}")
print(f"ISS :   R${calcula_imposto.realizaCalculo(orc, iss)}")