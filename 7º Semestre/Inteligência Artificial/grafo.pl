% FATOS %

arco(a, b, 3).
arco(b, a, 3).

arco(a, c, 4).
arco(c, a, 4).

arco(a, d, 5).
arco(d, a, 5).

arco(b, d, 2).
arco(d, b, 2).

arco(c, d, 4).
arco(d, c, 4).

arco(c, f, 5).
arco(f, c, 5).

arco(d, e, 2).
arco(e, d, 2).

arco(f, e, 2).
arco(e, f, 2).

arco(f, g, 1).
arco(g, f, 1).

% REGRAS %

conectado(X, Y, Z) :- arco(X, Y, Z).

vertice(X) :- arco(X, _, _).

caminho_1_passo(X, Y, Z, C) :- conectado(X, Y, C1), conectado(Y, Z, C2), (X \= Y), (Y \= Z), C is C1 + C2.
caminho_2_passos(X, Y, Z, A, C) :- conectado(X, Y, C1), conectado(Y, Z, C2), conectado(Z, A, C3), (X \= Y), (Y \= Z), (Z \= A), C is C1 + C2 + C3.
