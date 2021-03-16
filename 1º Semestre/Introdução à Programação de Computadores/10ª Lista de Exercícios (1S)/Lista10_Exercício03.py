x = int(input('X -> '))
n = int(input('N -> '))

print('Números congruentes:')

for m in range(1, 51):
    if m % x == n % x:
        print(f'{m} é congruente módulo {x} a {n}')
        