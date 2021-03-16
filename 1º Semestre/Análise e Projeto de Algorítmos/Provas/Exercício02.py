arr = [] 
simetrico = True
index = 0

print('Digite 20 elementos:')
for i in range(20):
    arr.append(int(input('-> ')))

while simetrico:
    if index > 10: 
        break
    if arr[index] == arr[19-index]:
        simetrico = True
    else:
        simetrico = False
    index += 1

print(arr)
if simetrico: 
    print(f'Vetor simétrico!')
else:
    print(f'Vetor não simétrico!')



