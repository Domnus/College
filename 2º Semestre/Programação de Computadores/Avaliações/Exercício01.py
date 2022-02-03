def maiorMenor(a, b):
    if a > b:
        print(f"O maior é {a}.")
    elif b > a:
        print(f"O maior é {b}.")
    else:
        print("Os dois são iguais.")

a, b = input("Escreva dois números: ").split(" ")

a = int(a)
b = int(b)

maiorMenor(a, b)
