from functools import reduce

list = [1, 2, 3, 4, 5]


def soma(x, y):
    return x + y


soma = reduce(soma, list, 10)
soma10 = reduce(soma, list, 10)

print(soma)
print(soma10)
