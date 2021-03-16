nomes = input("Digite os nomes separados por um espaço: ")

coca = nomes.split(" ")

coca.sort()

for i in range(len(coca)):
    print(f"{coca[i]}")
    