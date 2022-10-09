from functools import reduce
import time
start_time = time.time()

def pipe(f, g):
    return g(f)


def soma(x, y):
    return x + y


class Item():
    def __init__(self, id, produto, preco):
        self.id = id
        self.produto = produto
        self.preco = preco

    def getPreco(self):
        return self.preco


class Carrinho():
    def __init__(self):
        self.itens = []
        self.total = 0  # type: ignore

    def adicionar(self, item):
        self.itens.append(item)
        self.total += item.preco

    def remover(self, item):
        self.itens.remove(item)
        self.total -= item.preco

    def getTotal(self):
        return  pipe(list(map(lambda item: item.getPreco(), self.itens)), sum)


def main():
    carrinho = Carrinho()
    carrinho.adicionar(Item(1, 'Iphone', 499))
    carrinho.adicionar(Item(2, 'Kindle', 179))
    carrinho.adicionar(Item(3, 'Macbook Pro', 1199))
    print(f"O total do carrinho é: R${carrinho.getTotal()}")

main()
end_time = time.time()
elapsed_time = (end_time - start_time) * 10**3
print(f"Tempo de execução: {elapsed_time * 1000:.03f}ms")