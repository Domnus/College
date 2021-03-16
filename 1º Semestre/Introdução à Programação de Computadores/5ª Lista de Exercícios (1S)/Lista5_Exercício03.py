# 3-Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

soma = 0
x = 1
i = 0
while i < 50:
    if x % 2 == 0:
        soma += x
        i += 1
    x += 1

print(soma)
