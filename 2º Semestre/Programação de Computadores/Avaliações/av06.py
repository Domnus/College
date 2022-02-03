# Alisson Juan Feitoza RA: 601081
# Bento Carlos Silva dos Santos RA: 600784
# Fernando Cremonez Costa RA: 604097

from colorama import Fore
from colorama import Back
from colorama import Style

contatos = []

print(f"{Fore.BLUE}entrada{Style.RESET_ALL}")
n = int(input(""))

for i in range(n):
    pessoa = input("").capitalize()

    if pessoa in contatos:
        contatos.remove(pessoa)
    contatos.insert(0, pessoa)

print(f"{Fore.GREEN}resultado{Style.RESET_ALL}")
for pessoa in contatos:
    print(pessoa)
