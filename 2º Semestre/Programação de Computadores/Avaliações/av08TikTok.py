# Bento Carlos S. dos Santos---RA: 600784
# Frederico Hanai--------------RA: 604593

from random import randint
import os

try:
    os.mkdir("/home/bentocarlos/Documents/Github/Learning-Code/College/2ª Semestre/Programação de Computadores/Avaliações/input/")
    os.mkdir("/home/bentocarlos/Documents/Github/Learning-Code/College/2ª Semestre/Programação de Computadores/Avaliações/output")
except:
    Exception

try:
    for i in range(1,101):
        nome_arquivo = f"A_{i}.txt"
        file_input = open("/home/bentocarlos/Documents/Github/Learning-Code/College/2ª Semestre/Programação de Computadores/Avaliações/input/" + nome_arquivo, "w")

        x = randint(1, 105)
        file_input.write(f"{str(x)}\n")

        for i in range(x):
            z = randint(1,2)
            file_input.write(f"{z} ")
        
        file_input.write('\n')
        file_input.close()

    for i in range(1, 101):
        A = False
        B = False
        arquivo_input = f"A_{i}.txt"
        arquivo_output = f"A_{i}.txt"
        file_input = open(
            "/home/bentocarlos/Documents/Github/Learning-Code/College/2ª Semestre/Programação de Computadores/Avaliações/input/" + arquivo_input, "r")
        file_output = open(
            "/home/bentocarlos/Documents/Github/Learning-Code/College/2ª Semestre/Programação de Computadores/Avaliações/output/" + arquivo_output, "w")

        for i, line in enumerate(file_input):
            if i == 1:
                line = line.split()
                for lamp in line:
                    if int(lamp) == 1:
                        A = not(A)
                    else:
                        A = not(A)
                        B = not(B)
                if A:
                    file_output.write('1\n')
                else:
                    file_output.write('0\n')
                if B:
                    file_output.write('1\n')
                else:
                    file_output.write('0\n')

        file_input.close()
        file_output.close()

except IOError:
    print("Algum arquivo não foi encontrado!")
