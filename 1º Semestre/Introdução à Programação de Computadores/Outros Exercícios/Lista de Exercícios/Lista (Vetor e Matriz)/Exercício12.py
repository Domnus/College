arr = [0] * 50

for i in range(50):
    arr[i] = (i+5*i) % (i+1)

print(arr)