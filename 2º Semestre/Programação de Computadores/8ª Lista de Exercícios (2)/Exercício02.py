file = input("Digite o arquivo desejado: ")

try:
    file = open(file, 'r')
    lines = file.readlines()
    print(f"O arquivo tem {len(lines)} linhas")
except IOError:
    print("Arquivo não encontrado!")

