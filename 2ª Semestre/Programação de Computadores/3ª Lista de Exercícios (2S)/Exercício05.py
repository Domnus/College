def primoOuNao(num):
    if num == 1:
        return False
    for i in range(2, num//+1):
        if num % i == 0:
            return False
    return True

n = int(input("Digite um número: "))

for i in range(1,n):
    if primoOuNao(i):
        print(i)
