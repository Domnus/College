idade = 0
i = 0
c = True

while c:
    id = int(input('Digite a idade: '))
    if id > 0:
        idade += id
        i += 1
    c = id != 0


if i == 0:
    print('Não houve idades digitadas.')
else:
    media = idade / i
    print(f'A média é {media:.2f}')
    