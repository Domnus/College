% Grafo da Alegria !!!

% FATOS
% Arestas do grafo
aresta(a,b).
aresta(a,c).
aresta(b,d).
aresta(b,e).
aresta(c,f).
aresta(c,g).
aresta(d,h).
aresta(e,i).
aresta(e,j).
aresta(f,k).
aresta(h,d).

% nos objetivos
final(j).
final(f).

% Regras
%
%  **** BUSCA EM PROFUNDIDADE COM CICLOS E LIMITE ****
s(N, N1) :- aresta(N, N1).
resolva(Node, Solucao, Limite) :- depthFirstLimited([], Node, Solucao, Limite).

depthFirstLimited(Caminho, Node, [Node|Caminho], _) :- final(Node).
depthFirstLimited(Caminho, Node, Solucao, Limite) :- Limite > 0,
    s(Node, Node1),
    \+ pertence(Node1, Caminho),
    L1 is Limite - 1,
    depthFirstLimited([Node|Caminho], Node1, Solucao, L1).

pertence(E, [E|_]).
pertence(E, [_|T]) :- pertence(E, T).
