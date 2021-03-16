import random

pila = float(input('Valor da aposta: R$'))
num = int(input('Número a ser apostado (1 a 36): '))

if num < 1 or num > 36: 
    print('Número inválido! Fim de jogo!')
else:
    x = random.randint(1,36)
    x = 23
    if num == x:
        print(f'Parabéns! Você ganhou a aposta e ganhou R${pila*5}!')
    elif (num // 12)-1 == (x // 12)- 1: #((num >= 1 and num <= 12) and (x >=1 and x <= 12)) or ((num >= 13 and num <= 24) and (x >=13 and x <= 24)) or ((num >= 25 and num <= 36) and (x >=25 and x <= 36)):
        print(f'Parabéns! Você acertou a dúzia e ganhou R${pila*3}!') 
    elif (num % 2) == (x % 2):
        print(f'Parabéns! Você acertou a paridade e ganhou R${pila*2}!') 
    else:
        print('Mais sorte na próxima vez!')