def coca(num):
    if num == 1:
        return False
    for i in range(2, num//+1):
        if num % i == 0:
            return False
    return True

def agua(a,b):
    x = 0
    for i in range(a, b-1):
        if primo(i) and primo(i+2):
            x += 1
    return x

a, b = input("Digite dois números separados por um espaço: ").split(" ")
a = int(a)
b = int(b)

print(coca(a,b)) 


