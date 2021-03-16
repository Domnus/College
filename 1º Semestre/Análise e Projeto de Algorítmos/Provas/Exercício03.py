arr = [0] * 7

for i in range(7):
    arr[i] = [0] * 7
    
for i in range(7):
    for j in range(7):
        if i >=j:
            arr[i][j] = i ** 2 
        else:
            arr[i][j] = j ** 2
        
for i in range(7):
    for j in range(7):
        print(f'{arr[i][j]:2}', end=' ')
    print()
    
    