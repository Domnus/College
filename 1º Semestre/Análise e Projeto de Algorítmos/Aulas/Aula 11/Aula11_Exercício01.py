A = []
a = 0
b = 0

print('Digite 20 valores: ')
for i in range(20):
    A.append(int(input('-> ')))

print(A)

for i in range(10):
    A[i], A[i + 10] = A[i + 10], A[i]
    '''
    a = A[i]
    b = A[(i + 10)]
    A[i] = b
    A[i + 10] = a
    '''

print(A)