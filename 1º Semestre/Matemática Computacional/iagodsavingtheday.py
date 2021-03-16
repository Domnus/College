#Iagod salvando o dia
def div():
    print('A DIV B')
    a,b = input('Insira os numeros no formato A,B ->').split(',')
    a = int(a)
    b = int(b)
    d = a // b
    print('Div = {}'.format(d))
def mod():
    print('A MOD B')
    a, b = input('Insira os numeros no formato A,B ->').split(',')
    a = int(a)
    b = int(b)
    m = a % b
    print('Mod = {}'.format(m))
def cong():
    print('A ≡ B(MOD C)')
    a,b,c = input('Insira os numeros no formato A,B,C ->').split(',')
    a = int(a)
    b = int(b)
    c = int(c)
    con = (a - b) % c
    print('{} ≡ {} (Mod {}) = {}'.format(a,b,c,con))
def cr():
    x,y = input('Insira a range no formato COMEÇO,FIM -> ').split(',')
    x = int(x)
    y = int(y) + 1
    a = input('Insira o M ->')
    a = int(a)
    list = []
    for i in range(0, a):
        list.append([])
        for j in range(x, y):
            if (j - i) % a == 0:
                list[i].append(j)

    for i in range(0, a):
        print('[{}] : '.format(i), end='')
        for j in range(0, (len(list[i]))):
            print('[{:4}]'.format(list[i][j]), end='')
        print()
while True:
    print('Modulo = Mod / Divisor = Div / Congruencia = Cong / Classe de Residuo = Cr / Se desejar encerrar digite CLOSE')
    seila = input('Insira a operação desejada ->').upper()
    if seila == 'MOD':
        mod()
    if seila == "DIV":
        div()
    if seila == "CR":
        cr()
    if seila == 'CONG':
        cong()
    if seila == 'CLOSE':
        print('Obrigado por usar o IAGODSAVINGTHEDAY.PY')
        break