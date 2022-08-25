from random import randint
from time import sleep
from Processo import Processo
from datetime import datetime
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def tempo_execucao():
	return randint(1, 10) * 5


def prioridade():
	return randint(1, 5)


def printao(pilha, time_slice):
	cls()
	cabecalho = ["Process ID", "Tempo Entrada", "Tempo de Execução", "Prioridade"]

	print("|-------------------------------------------------------------|")
	print(f"| {cabecalho[0]} | {cabecalho[1]} | {cabecalho[2]} | {cabecalho[3]} |")

	for item in pilha:
		print("|------------+---------------+-------------------+------------|")

		cabecalhoProcess = str(len(cabecalho[0]) + 2)
		print(f"|{item.id:^{cabecalhoProcess}}", end="")

		tempo_entrada = item.tempo_entrada.strftime("%H:%M:%S")
		cabecalhoTempoEntrada = str(len(cabecalho[1]) + 2)
		print(f"|{tempo_entrada:^{cabecalhoTempoEntrada}}", end="")

		cabecalhoTempoExecucao = str(len(cabecalho[2]) + 2)
		print(f"|{item.tempo_execucao:^{cabecalhoTempoExecucao}}", end="")

		cabecalhoPrioridade = str(len(cabecalho[3]) + 1)
		print(f"| {item.prioridade:^{cabecalhoPrioridade}}|")

	print("|-------------------------------------------------------------|")
	print(f"Time Slice: {time_slice}		CPU: [{pilha[0].id}]")
	

if __name__ == "__main__":
	pilha = []
	contadorId = 1
	time_slice = 5
	while True:
		res = input("Deseja adicionar um processo? (s/n) ").lower()[0]
		if res == 's':
			pilha.append(Processo(contadorId, datetime.now(), tempo_execucao(), prioridade()))
			contadorId += 1
		elif res == 'n':
			pass
		else: 
			print("Opção inválida!")
			continue

		if len(pilha) > 0:
			pilha.sort(key=lambda x: (x.prioridade, x.tempo_entrada), reverse=True)
			printao(pilha, time_slice)

			if pilha[0].prioridade > 1:
				pilha[0].prioridade -= 1

			pilha[0].tempo_execucao -= time_slice
			if pilha[0].tempo_execucao <= 0:
				pilha.pop(0)

			pilha.sort(key=lambda x: (x.prioridade, x.tempo_entrada), reverse=True)
		else:
			print("Todos os processos foram executados.")
			break
		sleep(1)