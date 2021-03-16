from random import randint
maior = 0
menor = 51

x = 0
while x < 20:
    n = randint(1,50) 
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    x += 1

print(f'O maior é {maior}. O menor é {menor}')
    


