inicio, fim = input('Digite dois números: [x,x] ').split(',')
inicio = int(inicio)
fim = int(fim)

soma = 0
mult = 1

if fim < inicio:
    x = inicio
    inicio = fim
    fim = x


for i in range(inicio, fim+1):
    if i % 2 == 0:
        soma += i
    else:
        mult *= i

print(f'Soma: {soma}\nMultiplicação: {mult}')