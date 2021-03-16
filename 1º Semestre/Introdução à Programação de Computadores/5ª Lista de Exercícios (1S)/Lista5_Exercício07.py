# Faça um programa que calcule e escreva o valor de S:
# S= 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

i = 1
j = 1
soma = 0

while i < 51 and j < 100:
    soma += j/i
    j += 2
    i += 1

print(soma)
    
            
        