from random import randint
from cls import cls


class Grafo:
    def __init__(self, dict_grafo=None, direcionado=False):
        self.direcionado = direcionado
        if dict_grafo is None:
            self.dict_grafo = {}
        else:
            self.dictGrafo = dict_grafo

    def get_vertices(self):
        return list(self.dictGrafo.keys())

    def get_arestas(self):
        return list(self.dictGrafo.values())

    def verticeAleatorio(self):
        vertices = self.get_vertices()
        return randint(0, len(vertices) - 1)

    def find_path(self, vertice_inicial, vertice_final, path=None):
        if path is None:
            path = []
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
                caminhos.sort(key=len)
                if len(caminhos) == 0:
                    return False

        return True

    def busca_profunda(self):
        visitados = []
        pilha = []

        vertices = self.get_vertices()
        vertice_aleatorio = self.verticeAleatorio()

        pilha.append(vertices[vertice_aleatorio])
        visitados.append(vertices[vertice_aleatorio])

        while len(pilha) > 0:
            cls()
            vert_a = pilha.pop()

            print(f"Vértice atual: {vert_a}")
            print(f"Pilha: {pilha}")
            print(f"Visitados: {visitados}")

            input("Pressione ENTER para continuar...")

            for vertB in self.dictGrafo[vert_a]:
                if vertB not in visitados:
                    visitados.append(vertB)
                    pilha.append(vert_a)
                    pilha.append(vertB)

                    break

    def verificar_ciclo(self, vertice, visitados, primeiro_vertice, caminho=None):
        if caminho is None:
            caminho = []
        visitados.append(vertice)
        caminho.append(vertice)
        caminho_achado = False
        for verticeAdjacente in self.dictGrafo[vertice]:
            if caminho_achado:
                return [caminho, True]
            if verticeAdjacente not in visitados:
                caminho = self.verificar_ciclo(verticeAdjacente, visitados, vertice, caminho)
                if caminho is None:
                    return [caminho, False]
                if caminho[1]:
                    return [caminho[0], True]
            elif primeiro_vertice != verticeAdjacente:
                caminho.append(verticeAdjacente)
                caminho_achado = True

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
        tabela_direcionada = []
        tabela_nao_direcionada = []

        for vertice in grafo:
            for verticeAdjacente in grafo[vertice]:
                repetido = False
                for aresta in tabela_direcionada:
                    if verticeAdjacente == aresta[0][1] and vertice == aresta[0][0] or verticeAdjacente == aresta[0][0] and vertice == aresta[0][1]:
                        repetido = True
                        break
                if not repetido:
                    tabela_direcionada.append([[vertice, verticeAdjacente], grafo[vertice][verticeAdjacente]])
                tabela_nao_direcionada.append([[vertice, verticeAdjacente], grafo[vertice][verticeAdjacente]])

        tabela_direcionada.sort(key=lambda aresta_lambda: aresta_lambda[1])
        tabela_nao_direcionada.sort(key=lambda aresta_lambda: aresta_lambda[1])
        return tabela_direcionada, tabela_nao_direcionada

    def kruskal(self):
        tabela_direcionada, tabela_nao_direcionada = self.tabelaKruskal()
        agm = {}

        for aresta in tabela_nao_direcionada:
            if aresta[0][0] not in agm:
                agm[aresta[0][0]] = {}
            if aresta[0][1] not in agm:
                agm[aresta[0][1]] = {}

            agm[aresta[0][0]][aresta[0][1]] = aresta[1]
            agm[aresta[0][1]][aresta[0][0]] = aresta[1]

            agm_grafo = Grafo(agm, self.direcionado)

            if agm_grafo.achar_ciclo():
                agm[aresta[0][0]].pop(aresta[0][1])
                continue

            vertice_grafo_original = self.get_vertices()
            vertice_agm = agm_grafo.get_vertices()

            if len(vertice_grafo_original) == len(vertice_agm):
                if agm_grafo.validacaoConexo():
                    self.dictGrafo = agm_grafo.dictGrafo
                    return agm_grafo

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
            ordem_topologica = []

            fila = []
            graus = self.getGrauVertice()

            for vertice in graus:
                if graus[vertice] == 0:
                    fila.append(vertice)

            while len(fila) > 0:
                vertice = fila.pop(0)
                ordem_topologica.append(vertice)

                for verticeAdjacente in grafo[vertice]:
                    graus[verticeAdjacente] -= 1
                    if graus[verticeAdjacente] == 0:
                        fila.append(verticeAdjacente)

            if len(ordem_topologica) == len(self.get_vertices()):
                return True
