from random import randint
arr = [0] * 5
x = []
y = 1
for i in range(5):
    arr[i] = [0] * 5
    for j in range(5):
        arr[i][j] = randint(0, 9)

for i in range(5):
    for j in range(5):
        print(f'[{arr[i][j]}]', end= '')
    print()

print('Triângulo Inferior Direito:')

for i in  range(1, 5):
    for j in range(5 - i, 5):
        x.append(arr[i][j])
        if len(x) == y:
            print(x)
            x = []
            y += 1
        
