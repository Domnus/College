x = True
a = 0
b = 0
c = 0

while x:
    A = int(input('Digite um número-> (A) '))
    B = int(input('Digite um número-> (B) '))
    C = int(input('Digite um número-> (C) '))
    if A != B and B == C:
        a += 1
        print(f'O jogador A ganhou esta rodada!')
    elif B != A and A == C:
        b += 1
        print(f'O jogador B ganhou esta rodada!')
    elif C != B and B == A:
        c += 1
        print(f'O jogador C ganhou esta rodada!')
    if a == 3: 
        print('O jogador A é o vencedor!')
        x = False
    if b == 3:
        print('O jogador B é o vencedor!')
        x = False
    if c == 3:
        print('O jogador C é o vencedor!')
        x = False



