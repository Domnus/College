cond = True

while cond:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    op = input('Informe a operação: ')
    if op == '+':
        r = n1 + n2
        print(r)
    if op == '-': 
        r = n1 - n2
        print(r)
    if op == '*':
        r = n1 * n2
        print(r)
    if op == '/':
        r = n1 / n2
    cond = (n1 != '#') or 