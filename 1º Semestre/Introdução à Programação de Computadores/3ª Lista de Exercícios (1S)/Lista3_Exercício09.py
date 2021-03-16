farinha = int(input('Quantidade de xícaras de farinha de trigo: '))
ovos = int(input('Quantidade de ovos: '))
leite = int(input('Quantidade de colheres de leite: '))

A = farinha // 2
B = ovos // 3
C = leite // 5

if A<B<C:
    print(f'Será possível fazer {A} bolos.')
elif B<C:
    print(f'Será possível fazer {B} bolos.')
else:
    print(f'Será possível fazer {C} bolos.')