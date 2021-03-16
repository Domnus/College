from random import randint

n = randint(1, 101)
cont = 1
acertou = False

while not acertou:
    aposta = int(input('Digite um número: '))
    if aposta > n:
        print('Menor!')
        cont += 1
    if aposta < n:
        print('Maior!')
        cont += 1
    if aposta == n:
        print(f'Parabéns! Você acertou o número! Você tentou {cont} vezes!')
        acertou = True






