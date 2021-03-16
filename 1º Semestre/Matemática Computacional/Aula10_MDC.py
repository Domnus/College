num = int(input())
a = 1
num2 = int(input())
b = 1

L1 = []
L2 = []

while a < num:
  if num % a == 0:
    L1.append(a) 
  a += 1
print()

while b < num2:
  if num2 % b == 0:
    L2.append(b)
  b += 1  
for i in L1:
  if i in L2:
    print(i)

print('Iagod')