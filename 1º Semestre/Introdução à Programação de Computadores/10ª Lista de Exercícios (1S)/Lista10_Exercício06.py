from random import randint as rd

A = []
B = []


for i in range(10):
    A.append(rd(0, 10))

for i in range(10):
    holder = 0
    for j in range(i+1):
        holder += (j+1) * A[j]            
    B.append(holder)
    
print(A) 
print(B)

