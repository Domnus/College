def indices_pares(*w):
    return w[0][::2]

x = list(map(int, input("Digite os números: ").split()))
print(indices_pares(x))