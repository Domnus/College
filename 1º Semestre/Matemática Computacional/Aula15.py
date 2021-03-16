print("Classes de Resíduo\n")

m = int(input("Digite o valor do módulo (m): "))

for i in range(0,m):
    print(f"[{i}] = ", end = "{..., ")
    for x in range (-10,10):
        print(f"{m*x + i:^3},", end = " ")
    print("...}")