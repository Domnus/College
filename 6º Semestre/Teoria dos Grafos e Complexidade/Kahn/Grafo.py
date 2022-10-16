from random import randint

from cls import cls

class Grafo:
    def __init__(self, dictGrafo = None, direcionado = False):
        self.direcionado = direcionado
        if dictGrafo == None:
            dictGrafo = {}
        else:
            self.dictGrafo = dictGrafo


    def get_vertices(self):
        return list(self.dictGrafo.keys())


    def get_arestas(self):
        return list(self.dictGrafo.values())


    def verticeAleatorio(self):
        vertices = self.get_vertices()
        return randint(0, len(vertices) - 1)


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
    
    def validacaoConexo(self):
        grafo = self.dictGrafo
        arestas = self.get_arestas()
        contador = 0
        for aresta in arestas:
            if len(aresta) == 0:
                contador += 1
        
        if len(arestas) == contador:
            print("O grafo não tem arestas")
            return False
        
        vertices = self.get_vertices()
        for vertA in vertices:
            for vertB in vertices:
                caminhos = self.find_path(vertA, vertB)
                caminhos.sort(key = len)
                if len(caminhos) == 0:
                    return False
        
        return True


    def busca_profunda(self):
        visitados = []
        pilha = []

        vertices = self.get_vertices()
        verticeAleatorio = self.verticeAleatorio()

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


    def verificar_ciclo(self, vertice, visitados, primeiroVertice, caminho = []):
        visitados.append(vertice)
        caminho.append(vertice)
        caminhoAchado = False
        for verticeAdjacente in self.dictGrafo[vertice]:
            if caminhoAchado:
                return [caminho, True]
            if verticeAdjacente not in visitados:
                caminho = self.verificar_ciclo(verticeAdjacente, visitados, vertice, caminho)
                if caminho == None:
                    return [caminho, False]
                if caminho[1]:
                    caminhoAchado = True
                    return [caminho[0], True]
            elif primeiroVertice != verticeAdjacente:
                caminho.append(verticeAdjacente)
                caminhoAchado = True


    def achar_ciclo(self):
        vertices = self.get_vertices()
        visitados = []

        if len(vertices) > 2:
            for vertice in vertices:
                if vertice not in visitados:
                    caminho = self.verificar_ciclo(vertice, visitados, vertice)
                    if caminho is not None:
                        if caminho[1]:
                            return True
        return False

    def tabelaKruskal(self):
        grafo = self.dictGrafo
        tabelaDirecionada = []
        tabelaNaoDirecionada = []

        for vertice in grafo:
            for verticeAdjacente in grafo[vertice]:
                repetido = False
                for aresta in tabelaDirecionada:
                    if verticeAdjacente == aresta[0][1] and vertice == aresta[0][0] or verticeAdjacente == aresta[0][0] and vertice == aresta[0][1]:
                        repetido = True
                        break
                if not repetido:
                    tabelaDirecionada.append([[vertice, verticeAdjacente], grafo[vertice][verticeAdjacente]])
                tabelaNaoDirecionada.append([[vertice, verticeAdjacente], grafo[vertice][verticeAdjacente]])

        tabelaDirecionada.sort(key = lambda aresta: aresta[1])
        tabelaNaoDirecionada.sort(key = lambda aresta: aresta[1])
        return tabelaDirecionada, tabelaNaoDirecionada


    def kruskal(self):
        tabelaDirecionada, tabelaNaoDirecionada = self.tabelaKruskal()
        agm = {}

        for aresta in tabelaNaoDirecionada:
            if aresta[0][0] not in agm:
                agm[aresta[0][0]] = {}
            if aresta[0][1] not in agm:
                agm[aresta[0][1]] = {}

            agm[aresta[0][0]][aresta[0][1]] = aresta[1]
            agm[aresta[0][1]][aresta[0][0]] = aresta[1]

            agmGrafo = Grafo(agm, self.direcionado)

            if agmGrafo.achar_ciclo():
                agm[aresta[0][0]].pop(aresta[0][1])
                continue

            verticeGrafoOriginal = self.get_vertices()
            verticeAGM = agmGrafo.get_vertices()

            if len(verticeGrafoOriginal) == len(verticeAGM):
                if agmGrafo.validacaoConexo():
                    self.dictGrafo = agmGrafo.dictGrafo
                    return agmGrafo
                


    def getGrauVertice(self):
        vertices = self.get_vertices()
        graus = {}
        for vertA in vertices:
            contador = 0
            for vertB in vertices:
                if vertA in self.dictGrafo[vertB]:
                    contador += 1
            graus[vertA] = contador
        return graus


    def validarKahn(self):
        if not self.direcionado:
            return None
        else:
            grafo = self.dictGrafo
            ordemTopologica = []

            fila = []
            graus = self.getGrauVertice()

            for vertice in graus:
                if graus[vertice] == 0:
                    fila.append(vertice)

            while len(fila) > 0:
                vertice = fila.pop(0)
                ordemTopologica.append(vertice)

                for verticeAdjacente in grafo[vertice]:
                    graus[verticeAdjacente] -= 1
                    if graus[verticeAdjacente] == 0:
                        fila.append(verticeAdjacente)

            if len(ordemTopologica) == len(self.get_vertices()):
                return True