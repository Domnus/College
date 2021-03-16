def openFile():
        return open('notas_estudantes.txt', 'r')

def mais6Notas():
        file = openFile()
        print('----------------')
        for line in file:
            data = line.split()
            if len(data) > 7:
                print(f"-> {data[0]} tem mais de 6 notas")

def mediaNotas():
    file = openFile()
    print('----------------')
    for line in file:
        data = line.split()
        nome = data[0]
        data = list(map(float, data[1:]))
        media = sum(data) / len(data)
        print(f"-> Média de {nome}: {media:.2f}")
    print('----------------')

def notaMaxMin():
    file = openFile()
    print('----------------')
    for line in file:
        data = line.split()
        nome = data[0]
        data = list(map(float, data[1:]))
        data.sort()
        print(f"-> {nome}: Nota máxima: {data[-1]} | Nota mínima: {data[0]}")
    print('----------------')

mais6Notas()
mediaNotas()
notaMaxMin()

