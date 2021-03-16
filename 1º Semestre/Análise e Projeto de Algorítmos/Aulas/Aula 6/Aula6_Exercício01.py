print('-----Média de notas-----')
alunos = 1
aprovados = 0
reprovados = 0
qmedia = 0
mgeral = 0

while alunos <=6:
    m1 = float(input('Primeira nota: '))
    if m1 > 10 or m1 < 0:
        print('Nota inválida!')
        m1 = 0
    m2 = float(input('Segunda nota: '))
    if m2 > 10 or m1 < 0:
        print('Nota inválida!')
        m2 = 0
    media = (m1 + m2) / 2
    qmedia += 1
    mgeral += media
    alunos +=1
    if media >= 7:
        print('Aluno aprovado.')
        aprovados += 1   
    elif media >= 0 and media < 7:
        print('Aluno reprovado.')
        reprovados += 1
    else:
        print('Média inválida!')

rmedia = mgeral / qmedia
print(f'Alunos aprovados: {aprovados} \nAlunos reprovados: {reprovados} \nMédia da classe: {rmedia:.2f}')
    
