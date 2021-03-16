print('-----Digite 3 números-----')
_A1 = input('-> ')
_A2 = input('-> ')
_A3 = input('-> ')
_A = (_A1, _A2, _A3)

print('-----Digite 4 letras-----')
_B1 = input('-> ')
_B2 = input('-> ')
_B3 = input('-> ')
_B4 = input('-> ')
_B = (_B1, _B2, _B3, _B4)

print(f'A = {_A}')
print(f'B = {_B}')

print(f' A x B:')
_cont1 = 0
_cont2 = 0
_cont3 = 0

for i in _A:
    for j in _B:
        print(f'({i}, {j})', end="")
        _cont1 += 1
    print()

print(' A x A: ')
for i in _A:
    for j in _A:
        print(f'({i}, {j})', end="")
        _cont2 += 1
    print()

print(' B x A: ')
for i in _B:
    for j in _A:
        print(f'({i},{j})', end="")
        _cont3 += 1
    print()

print(f'\nA x B = {_cont1}')
print(f'A x A = {_cont2}')
print(f'B x A = {_cont3}')