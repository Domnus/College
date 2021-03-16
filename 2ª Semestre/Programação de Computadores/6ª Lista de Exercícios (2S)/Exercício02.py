def quadrados(n):
    return list(map(lambda x: x*x, list(range(1, n+1))))

n = int(input("Digite um número: "))
print(f"{n} primeiros quadrados perfeitos: ", end="")
print(*quadrados(n))
        
