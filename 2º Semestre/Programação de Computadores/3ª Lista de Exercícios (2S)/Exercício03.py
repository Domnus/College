def contrario(word):
    drow = word[::-1]
    drow = int(drow)

    return drow

n = input("Digite um número:")

print(f"{n} ao contrário é {contrario(n)}")
