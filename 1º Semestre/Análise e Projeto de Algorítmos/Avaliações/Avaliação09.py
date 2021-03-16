N = int(input('Digite o número de elementos desejados para o vetor: \n-> '))
A = []

print('Digite os elementos desejados:')
for i in range(N):
    A.append(int(input('-> ')))

A.sort()

print(f'Vetor A: \n{A}')

V = int(input('Digite o valor que queira inserir no vetor: \n-> ')) 

if V > A[-1]:
    A.append(V)
elif V < A[0]:
    A.insert(0, V)
else:
    for i in range(len(A)):
        if A[i] > V:
            A.insert((i), V) 
            break

print(f'O novo vetor ficará assim: \n{A}')



