# Alisson Juan Feitoza RA: 601081
# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

def soma(A, B):
    if A < 1:
        A *= 10
    if B < 1:
        B *= 10

    if A < 10 and B < 10:
        return int(A) + int(B)
    return soma(A / 10, B / 10)

A, B = input("Digite dois números para soma: ").split(" ")
A = int(A)
B = int(B)

print(f"A soma dos primeiros dígitos é {soma(A,B)}")
