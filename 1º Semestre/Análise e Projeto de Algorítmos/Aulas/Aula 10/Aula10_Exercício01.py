a = []
print('Digite 10 números: ')
for i in range(1, 11):
    a.append(input('-> '))

a.sort()

print(f'O maior número da lista é {a[-1]} e o menor número é {a[0]}')
