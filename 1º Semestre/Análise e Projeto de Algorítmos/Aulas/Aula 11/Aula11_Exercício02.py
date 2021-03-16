print('-----20 primeiros números da série de Fibonacci-----')

'''
a = 0
b = 1
c = 1
A= []

for i in range(20):
    A.append(c)
    c = a + b
    a = b
    b = c
'''
A = [0]*20
A[0] = 1
A[1] = 1

for i in range(2, 20):
    A[i] = A[i - 1] + A[i - 2]

print(A)