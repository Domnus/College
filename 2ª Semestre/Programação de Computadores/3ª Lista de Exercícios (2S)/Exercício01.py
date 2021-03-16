def parOuImpar(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

num = int(input("Digite um número: "))

if parOuImpar(num):
    print("Número Par.")
else:
    print("Número Ímpar.")
