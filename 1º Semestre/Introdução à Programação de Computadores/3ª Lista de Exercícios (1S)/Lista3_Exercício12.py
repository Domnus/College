valor = int(input('Valor de bits a ser trocado: B$'))

n50 = valor // 50
n10 = valor % 50 // 10
n5 = valor % 50 % 10 // 5
n1 = valor % 50 % 10 % 5

print(f'O valor de B${valor:.2f} será trocado por ',end='')
if n50>0:
    print(f'{n50} notas de B$50,00 ',end='')
if n10>0:
    print(f'{n10} notas de B$10,00',end='')
if n5>0:
    print(f'{n5} notas de B$5,000',end='')
if n1>0:
    print(f'{n1} notas de B$1,00.',end='')