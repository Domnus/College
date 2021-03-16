arr = [0] * 5

for i in range(5):
    arr[i] = [0] * 10
    for j in range(5):
        if i % 2 == 0:
            arr[i][j] = j + 1
        elif i % 2 != 0:
            arr[i][j] = i + 1

print('=' * 15)
for i in range(5):
    for j in range(5):
        print(f'[{arr[i][j]}]', end='')
    print()
print('=' * 15)