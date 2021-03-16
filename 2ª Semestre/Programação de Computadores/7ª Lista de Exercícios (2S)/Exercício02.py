

print('Digite as informações do aluno: ')

def cadastro():
    while True:
        aluno.clear()
        aluno['RA'] = int(input('Digite o RA do aluno: '))
        aluno['nome'] = input('DIgite o nome do aluno: ')
        aluno['nota'] = int(input('Digite a nota do aluno: '))
        alunos.append(aluno.copy())
        
        x = input('Deseja continuar? S/N:').upper()
        if x == 'N':
            break

def Media():
    media = 0
    for a in alunos:
        media += a['nota']
    media /= len(alunos)
    print(f'Média da turma: {media}')

    return media

def acimaMedia(media):
    print('Alunos com nota maior ou igual a média:')
    for a in alunos:
        if a['nota'] >= media:
            print(f'Aluno = {a["nome"]} | Nota = {a["nota"]}')

def Maior():
    maior = 0
    nomeMaior = ''
    for a in alunos:
        if a['nota'] > maior:
            maior = a['nota']
            nomeMaior = a['nome']

    print(f'Aluno com a maior nota: {nomeMaior}')


alunos = []
aluno = {}

cadastro()

acimaMedia(Media())
Maior()





        
        
                

   
        

    
        
