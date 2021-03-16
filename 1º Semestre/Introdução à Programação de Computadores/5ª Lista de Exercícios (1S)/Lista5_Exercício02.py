# 2-Faça um programa que leia 10 inteiros e imprima sua média.

cont = 0
x = 0

for i in range(1, 11):
    n = int(input('Digite um valor-> '))
    x += n
    cont += 1

media = x / cont

print(f'A média é {media}')