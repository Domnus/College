from functools import reduce

lista = [1,2,3,4,5]

def sum(a, b):
    return (a + b)

soma = reduce(sum, lista)
soma10 = reduce(sum, lista, 10)
print(soma)
print(soma10)