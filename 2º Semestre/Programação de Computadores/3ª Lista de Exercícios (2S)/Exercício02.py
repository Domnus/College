def power(base, exp):
    p = 1
    for i in range(exp):
         p *= base
    print(p)

base, exp = input("Digite a base e o expoente, respectivamente: ").split(" ")
base = int(base)
exp = int(exp)

power(base, exp)
