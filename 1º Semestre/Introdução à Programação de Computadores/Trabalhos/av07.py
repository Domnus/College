from random import randint

_cont = 0
x = True

while x:
    n = randint(100, 999)
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    if a != b and  b!= c and a != c:
        x = False

print(n)
x = True

while x:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    _cont += 1
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    _menor = (a * 100) + (b * 10) + c

    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a

    _maior = (a * 100) + (b * 10) + c
    n = _maior - _menor
    if n == 495:
        x = False

print(f'Iterações: {_cont}')






