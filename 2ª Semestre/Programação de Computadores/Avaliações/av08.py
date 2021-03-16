# Bento Carlos S. dos Santos---RA: 600784
# Frederico Hanai--------------RA: 604593

from random import randint
import os

try:
    os.mkdir("input")
    os.mkdir("output")
except:
    Exception

try:
    for i in range(1,101):
        nome_arquivo = f"input/A_{i}"
        file_input = open(nome_arquivo,"w")

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
        arquivo_input = f"input/A_{i}"
        arquivo_output = f"output/A_{i}"
        file_input = open(arquivo_input,"r")
        file_output = open(arquivo_output, "w")

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
