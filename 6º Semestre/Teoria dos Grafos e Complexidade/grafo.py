# Andressa Caroline R. Bueno RA: 607290
# Bento Carlos S. dos Santos RA: 600784
# Frederico Hanai 			 RA: 604593
# Hugo Seiti Odajima 		 RA: 606537
# Paulo Guilherme Astrauskas RA: 548111

class Grafo:
	dictGrafo = {}

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


def validacao(grafo):
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
		
			
def printGrafo(grafo):
	for i in range(len(grafo)):
		for j in range(len(grafo[i])):
			print(grafo[i][j], end="")
		print("\n")


def main():
	vertices = []
	while vertices == []:
		vertices = input("Vértices do grafo: ").upper().split()
	arestas = []
	while True:
		res = input("Digite o par de vértices para as arestas [Digite 0 para parar]: ").upper().split()
		if res[0] == '0':
			break
		
		for aresta in res:
			if aresta not in vertices:
				print("Aresta inválida")
				continue
		arestas.append(res)

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

	#dictGrafo = {
	#	'V1': ['V2', 'V3'],
	#	'V2': ['V1', 'V3'],
	#	'V3': ['V1', 'V2', 'V4'],
	#	'V4': ['V3']
	#}
	grafo = Grafo(dictGrafo)

	if validacao(grafo):
		print("O grafo é conexo")
	else:
		print("O grafo não é conexo")


if __name__== "__main__":
	main()
