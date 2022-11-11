from copy import deepcopy
from math import inf
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


    def verificar_ciclo(self, vertice, primeiroVertice, caminho, visitados, primeiroAdjacente = None):
        visitados.append(vertice)
        caminho.append(vertice)
        cicloAchado = False
        for verticeAdjacente in self.dictGrafo[vertice]:
            if cicloAchado:
                return caminho, True
            if verticeAdjacente not in visitados:
                caminho, cicloAchado = self.verificar_ciclo(verticeAdjacente, primeiroVertice, deepcopy(caminho), deepcopy(visitados), vertice)
                if cicloAchado:
                    return caminho, True
            elif primeiroVertice == verticeAdjacente:
                caminho.append(verticeAdjacente)
                if len(caminho) > 3:
                    cicloAchado = True
                    return caminho, True
                else:
                    caminho.pop()
            if primeiroAdjacente == verticeAdjacente:
                continue

        caminho.pop()    
        return caminho, cicloAchado


    def achar_ciclo(self):
        vertices = self.get_vertices()
        cicloAchado = False

        for vertice in vertices:
            caminho = []
            visitados = []
            caminho, cicloAchado = self.verificar_ciclo(vertice, vertice, visitados, caminho)
            break

        return cicloAchado


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


    def prim(self):
        grafo = self.dictGrafo
        agm = {}
        grafo_ordenado = {}
        vertices = self.get_vertices()
        vertices_ciclo = []

        for vertice in grafo.keys():
            grafo_ordenado[vertice] = sorted(grafo[vertice].items(), key=lambda item: item[1])

        primeiro_vertice = list(grafo_ordenado.keys())[0]
        agm[primeiro_vertice] = {}

        while len(agm.keys()) != len(vertices):
            vertices_possiveis = {}
            vertices_seguros = []
            for vertice in agm.keys():
                for vertice_adjacente in grafo_ordenado[vertice]:
                    if vertice_adjacente[0] not in agm[vertice] and vertice_adjacente[0] not in vertices_possiveis:
                        if vertice not in vertices_possiveis:
                            vertices_possiveis[vertice] = {}
                        vertices_possiveis[vertice][vertice_adjacente[0]] = vertice_adjacente[1]

            for vertice in vertices_possiveis:
                for verticeAdjacente in vertices_possiveis[vertice]:
                    if len(agm.keys()) >= 2:
                        if [vertice, verticeAdjacente, vertices_possiveis[vertice][verticeAdjacente]] not in vertices_ciclo:
                            agm_temp = deepcopy(agm)
                            agm_temp[vertice][verticeAdjacente] = vertices_possiveis[vertice][verticeAdjacente]
                            agm_temp[verticeAdjacente] = {}
                            agm_temp[verticeAdjacente][vertice] = vertices_possiveis[vertice][verticeAdjacente]
                            agm_temp = Grafo(agm_temp, self.direcionado)
                            if not agm_temp.achar_ciclo():
                                vertices_seguros.append([vertice, verticeAdjacente, vertices_possiveis[vertice][verticeAdjacente]])
                            else:
                                vertices_ciclo.append([vertice, verticeAdjacente, vertices_possiveis[vertice][verticeAdjacente]])
                    else:
                        vertices_seguros.append([vertice, verticeAdjacente, vertices_possiveis[vertice][verticeAdjacente]])

            vertices_seguros.sort(key=lambda vertice_lambda: vertice_lambda[2])

            for vertice in vertices_seguros:
                if vertice[1] not in agm:
                    agm[vertice[1]] = {}
                agm[vertice[0]][vertice[1]] = vertice[2]
                agm[vertice[1]][vertice[0]] = vertice[2]
                break

        return agm

    def achar_menor_caminho(self, vInicial, vFinal):
        distanciasAcumuladas = {}
        anteriores = {}
        expandidos = []
        caminho = []
        vOrigem = ''
        grafo = self.dictGrafo

        for i in grafo:
            distanciasAcumuladas[i] = inf
            anteriores[i] = 0


        for vAdjacente in grafo[vInicial]:
            # grafo[vOrigem][vAdjacente] --> peso do vOrgiem pro vAdjacente
            # distanciasAcumuladas[vAdjacente] --> pega a distancia acumulada do vAdjacente
            if(grafo[vInicial][vAdjacente] < distanciasAcumuladas[vAdjacente]):
                distanciasAcumuladas[vAdjacente] = grafo[vInicial][vAdjacente]
                anteriores[vAdjacente] = vInicial
        expandidos.append(vInicial)

        # lista_DA = {v:DA}
        # distanciasAcumuladas --> dicionario
        # vertice --> chave (v)
        # distanciasAcumuladas[vertice] --> valor (DA)
        menor = inf
        for vertice in distanciasAcumuladas:
            if(distanciasAcumuladas[vertice] < menor and vertice not in expandidos):
                menor = distanciasAcumuladas[vertice]
                vOrigem = vertice

        while(vFinal not in expandidos):
            for vAdjacente in grafo[vOrigem]:
                if(vAdjacente in expandidos):
                    continue
                if (distanciasAcumuladas[vOrigem] + grafo[vOrigem][vAdjacente] < distanciasAcumuladas[vAdjacente]):
                    distanciasAcumuladas[vAdjacente] = distanciasAcumuladas[vOrigem] + grafo[vOrigem][vAdjacente]
                    anteriores[vAdjacente] = vOrigem
            expandidos.append(vOrigem)

            menor = inf
            for vertice in distanciasAcumuladas:
                if (distanciasAcumuladas[vertice] < menor and vertice not in expandidos):
                    menor = distanciasAcumuladas[vertice]
                    vOrigem = vertice

        vertice = vFinal
        caminho.append(vFinal)
        while(True):
            if(vertice != vInicial):
                caminho.append(anteriores[vertice])
                vertice = anteriores[vertice]
            else:
                break

        caminho.reverse()

        print("Caminho Mínimo: ", end="")
        for v in range (len(caminho)-1):
            print(f"{caminho[v]} => ", end="")
        print(vFinal)

        return True