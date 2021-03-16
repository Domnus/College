from random import randint as rd

num = rd(0, 6)
cor = rd(0, 1)

nome_cor = ['Preta', 'Branca']

print('Aposte um número e uma cor!')
while True:
    aposta_num, aposta_cor= input('[0 a 6] [0 = Preta, 1 = Branca] ->').split(',')
    aposta_num = int(aposta_num)
    aposta_cor = int(aposta_cor)
    if aposta_num not in range(7):
        print('Digite um número entre 0 e 6!')
    elif aposta_cor not in range(2):
        print('Digite um número entre 0 e 1!')
    else:
        break

if aposta_num == num and aposta_cor == cor:
    print(f'Você ganhou! Acertou a cor {nome_cor[aposta_cor]} e o número {num}!')
elif aposta_num == num and aposta_cor != cor:
    print(f'Voce acertou apenas o número {num}!')
elif aposta_num != num and aposta_cor == cor:
    print(f'Você acertou apenas a cor {nome_cor[aposta_cor]}!')
else:
    print('Você não acertou nada! Mais sorte na próxima!')