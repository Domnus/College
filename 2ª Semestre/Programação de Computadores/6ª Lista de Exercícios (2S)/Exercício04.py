from functools import reduce

def mult(x,y):
    return x * y

def prod_lista(*args):
    return reduce(mult,args[0])

valores = list(map(int, input("Digite os valores: ").split()))

print(f"O produto dos valores será {prod_lista(valores)}.")