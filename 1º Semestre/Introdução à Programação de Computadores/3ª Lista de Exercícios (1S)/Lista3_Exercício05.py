tl = float(input('Trabalho de Laboratório: '))
av = float(input('Avaliação Semestral: '))
ef = float(input('Exame Final: '))

m = ((float(tl) * 2.0) + (float(av) * 3.0) + (float(ef) * 5.0)) / 10

print(f'Média: {m}')

if m >= 0 and m <= 2.9:
    print('Aluno reprovado.')
elif m >= 3 and m <=4.9:
    print('Aluno de recuperação.')
else:
    print('Aluno aprovado.')