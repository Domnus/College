arr = [0] * 5

for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        if i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = 0

for i in range(4):
    for j in range(4):
        print(f'[{arr[i][j]:2}]', end=' ')
    print()