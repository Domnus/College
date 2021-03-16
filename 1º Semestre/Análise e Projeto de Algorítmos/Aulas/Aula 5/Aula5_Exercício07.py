print('Digite três valores: ')
a = int(input())
b = int(input())
c = int(input())

if ((a > b) or (a > c)):
    if (b < c):
        a, b = b, a
    else:
        a, c = c, a

if (b > c):
    b, c = c, b

print(f'A = {a}, B = {b}, C = {c}')

