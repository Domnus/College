l = []
print("Informe 10 números")
for i in range(10):
    l.append(int(input("{}º -> ".format(i+1))))
print(l)
print("\nNúmeros primos")
for i in range(10):
    p = True
    if l[i] < 2:
        p = False
    for j in range(2,l[i]//2+1):
        if l[i] % j == 0:
            p = False
            break
    if p:
        print("Número: {} - Posição: {}".format(l[i],i))