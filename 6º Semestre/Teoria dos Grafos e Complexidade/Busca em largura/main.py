# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Bruno Campos				 RA: 610453
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537

import os
from random import randint


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def build_grafo(vertices, arestas):
	dictGrafo = {}

	for vertice in vertices:
		dictGrafo[vertice] = {}
		arestasB = []
		for aresta in arestas:
			if vertice in aresta:
				vert = [x for x in aresta if x != vertice and x not in arestasB]
				if len(vert) > 0:
					arestasB.append(vert[0])
		dictGrafo[vertice] = arestasB 

	return dictGrafo


class Grafo:
	def __init__(self, dictGrafo = None):
		if dictGrafo == None:
			dictGrafo = {}
		else:
			self.dictGrafo = dictGrafo

	def get_vertices(self):
		return list(self.dictGrafo.keys())


	def get_arestas(self):
		return list(self.dictGrafo.values())


	def find_path(self, vertice_inicial, vertice_final, path=[]):
		grafo = self.dictGrafo
		path = path + [vertice_inicial]
		if vertice_inicial == vertice_final:
			return [path]
		if vertice_inicial not in grafo:
			return []
		paths = []
		for vertex in grafo[vertice_inicial]:
			if vertex not in path:
				extended_paths = self.find_path(vertex, vertice_final, path)
				for p in extended_paths: 
					paths.append(p)
		return paths


	def busca_profunda(self):
		visitados = []
		pilha = []

		vertices = self.get_vertices()
		verticeAleatorio = randint(0, len(vertices)-1)

		pilha.append(vertices[verticeAleatorio])
		visitados.append(vertices[verticeAleatorio])

		while len(pilha) > 0:
			cls()
			vertA = pilha.pop()

			print(f"Vértice atual: {vertA}")
			print(f"Pilha: {pilha}")
			print(f"Visitados: {visitados}")

			input("Pressione ENTER para continuar...")

			for vertB in self.dictGrafo[vertA]:
				if vertB not in visitados:
					visitados.append(vertB)
					pilha.append(vertA)
					pilha.append(vertB)
					
					break


	def busca_largura(self):
		grafo = self.dictGrafo
		vertices = self.get_vertices()
		visitados = []
		fila = []
		#verticeAleatorio = randint(0, len(vertices)-1)
		verticeAleatorio = 0

		for vertice in vertices:
			if vertice not in visitados:
				fila.append(vertice)
				visitados.append(vertice)

				while len(fila) > 0:
					vertA = fila.pop(0)

					for vertB in vertices:
						caminhos = self.find_path(vertA, vertB)
						caminhos.sort(key = len)
						caminho = caminhos[0]
						if vertB != vertA:

							if len(caminho) == 2:
								if vertB not in visitados:
									cls()
									print(f"Vértice atual: {vertA}")
									print(f"Fila: {fila}")
									print(f"Visitados: {visitados}")

									#input("Pressione ENTER para continuar...")
									print()
									visitados.append(vertB)
									fila.append(vertB)


	def validacaoComplexo(grafo):
		arestas = grafo.get_arestas()
		contador = 0

		for aresta in arestas:
			if len(aresta) == 0:
				contador += 1

		if len(arestas) == contador:
			print("O grafo não tem arestas")
			return False 

		vertices = grafo.get_vertices()
		for vertA in vertices:
			for vertB in vertices:
				caminhos = grafo.find_path(vertA, vertB)
				caminhos.sort(key = len)

				if len(caminhos) == 0:
					return False

		return True


def main():
	#vertices = []

	#while vertices == []:
	#	vertices = input("Vértices do grafo: ").upper().split()

	#arestas = []

	#while True:
	#	res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()
	#	if res[0] == '0':
	#		break
	#	
	#	for aresta in res:
	#		if aresta not in vertices:
	#			print("Aresta inválida")
	#			continue
	#	arestas.append(res)

	#dictGrafo = {
	#	'V1': ['V2', 'V3'],
	#	'V2': ['V1', 'V3'],
	#	'V3': ['V1', 'V2', 'V4'],
	#	'V4': ['V3']
	#}

	#dictGrafo = build_grafo(vertices, arestas)

	dictGrafo = {
		'A': ['D', 'E', 'B'],
		'D': ['A', 'E', 'G'],
		'E': ['A', 'B', 'D'],
        'B': ['A', 'C', 'E'],
		'G': ['D', 'H'],
		'C': ['B', 'F'],
		'H': ['F', 'I', 'G'],	
		'F': ['C', 'H', 'I'],
		'I': ['F','H']	
	}

	grafo = Grafo(dictGrafo)
	grafo.busca_largura()


if __name__== "__main__":
	main()