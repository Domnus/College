def primo(num):
    if num == 1:
        return False
    for i in range(2, num//+1):
        if num % i == 0:
            return False
    return True

def superPrimo(num):
    x = num 
    while x > 0:
        if not primo(x):
            return False
        x //= 10
    return True

num = int(input("Digite um número: "))
start = 10**(num - 1)
finish = 10**num

for i in range(start, finish):
    if superPrimo(i):
        print(f"{i}")
    



