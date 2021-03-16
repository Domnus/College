def primoOuNao(num):
    if num == 1:
        return False
    for i in range(2, num//+1):
        if num % i == 0:
            return False
    return True

num = int(input("Digite um número: "))
if primoOuNao(num):
    print("Número Primo.")
else:
    print("Não primo.")
