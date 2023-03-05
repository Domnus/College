class Imposto(object):
    def calcula():
        pass


class item(object):
    def __init__(self, valor, nome):
        self.valor = valor
        self.nome = nome


class imposto(object):
    def __init__(self):
        self.total = 0
        self.itens = []

    def icms(self):
        return self.total * 0.20

    def pis(self):
        return self.total * 0.05

    def cofins(self):
        return self.total * 0.03

    def iss(self):
        return self.total * 0.02

    def adiciona_item(self, item):
        self.itens.append(item)
        self.calcula_total()

    def calcula_total(self):
        total = 0
        for item in self.itens:
            total += item.valor
        self.total = total

    def calcula_total_imposto(self):
        return self.total + self.icms() + self.pis() + self.cofins() + self.iss()

    def getTotal(self):
        return self.total


imposto = imposto()
imposto.adiciona_item(item(100, "Produto 1"))
imposto.adiciona_item(item(200, "Produto 2"))
imposto.adiciona_item(item(300, "Produto 3"))

print("Valor do produto: ", imposto.getTotal())
print("Valor do ICMS: ", imposto.icms())
print("Valor do PIS: ", imposto.pis())
print("Valor do COFINS: ", imposto.cofins())
print("Valor do ISS: ", imposto.iss())
print("Valor total com imposto: ", imposto.calcula_total_imposto())
