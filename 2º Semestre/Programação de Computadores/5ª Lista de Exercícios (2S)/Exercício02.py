from random import randint

A = []

for i in range(10):
    A.append(randint(1, 10))

def coca(lista, num):
    i = len(lista) 
    if i == 0:
        return False
    if lista[i-1] != num:
        return coca(lista[:i-1], num)
    return True

lista = input("Digite a matriz: ").strip()
lista = lista.split(' ')
num = input("Digite o número que deseja procurar: ")

if coca(lista, num):
    print(f"O número {num} está contido na lista {lista}")
else:
    print(f"O número {num} não está contido na lista {lista}")