from random import randint

A = []
B = []
C = []
i = 0

print('Digite os números desejados:')

for j in range(6):
    x = randint(1, 60)
    if x not in B:
        A.append(x)

while i < 6:
    x = int(input('-> '))
    if x < 1 or x > 60:
        print('Número inválido!')
        continue
    elif x in B:
        print('Número já digitado!')
    elif x not in B:
        B.append(x)
        i += 1

A.sort()
B.sort()

for i in A:
    if i in B:
        C.append(i)

print(f'Números sorteados: \n{A}')
if len(C) == 4:
    print(f'Parabéns! Você acertou a quadra! Esses foram os números que você acertou: \n{C}')
elif len(C) == 5:
    print(f'Parabéns! Você acertou a quina! Esses foram os números que você acertou: \n{C}')
elif len(C) == 6:
    print(f'Parabéns! Você acertou a sena! Esses foram os números que você acertou: \n{C}')
elif len(C) == 0:
    print('Infelizmente você não acertou nenhum número! Mais sorte na próxima vez!')
else:
    print(f'Você acertou {len(C)} número(s)! Aqui estão eles: \n{C}')
