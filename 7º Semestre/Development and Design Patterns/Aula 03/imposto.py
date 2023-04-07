#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Orcamento:
    def __init__(self, valor: float):
        self.valor = valor

    def getValor(self) -> float:
        return self.valor


class Imposto(ABC):
    @abstractmethod
    def calcula(self, orcamento: Orcamento) -> float:
        pass

    @abstractmethod
    def calcula_outro_imposto(self, orcamento: Orcamento) -> float:
        pass


class ISS(Imposto):
    outroImposto: Imposto | None

    def __init__(self, outroImposto=None):
        self.outroImposto = outroImposto

    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.getValor() * 0.07 + self.calcula_outro_imposto(orcamento)

    def calcula_outro_imposto(self, orcamento: Orcamento) -> float:
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)


class ICMS(Imposto):
    outroImposto: Imposto | None

    def __init__(self, outroImposto=None):
        self.outroImposto = outroImposto

    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.getValor() * 0.1 + self.calcula_outro_imposto(orcamento)

    def calcula_outro_imposto(self, orcamento: Orcamento) -> float:
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)


class PIS(Imposto):
    outroImposto: Imposto | None

    def __init__(self, outroImposto=None):
        self.outroImposto = outroImposto

    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.getValor() * 0.01 + self.calcula_outro_imposto(orcamento)

    def calcula_outro_imposto(self, orcamento: Orcamento) -> float:
        if self.outroImposto is None:
            return 0
        return self.outroImposto.calcula(orcamento)


impostoSimples = ISS()
impostoComplexo = ISS(ICMS(PIS()))
orcamento = Orcamento(500)

print(f"Imposto Simples : {impostoSimples.calcula(orcamento)}")
print(f"Imposto Complexo: {impostoComplexo.calcula(orcamento)}")
