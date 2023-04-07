% Fatos %
gerou(maria, jose).
gerou(joao, jose).
gerou(joao, ana).

gerou(jose, julia).
gerou(jose, iris).

gerou(iris, jorge).

homem(jose).
homem(joao).
homem(jorge).
homem(carlos).

mulher(maria).
mulher(ana).
mulher(iris).
mulher(julia).

casado(maria, joao).
casado(joao, maria).

casado(ana, carlos).
casado(carlos, ana).

% Regras %

pai(X, Y) :- gerou(X, Y), homem(X).
mae(X, Y) :- gerou(X, Y), mulher(X).

filho(X, Y) :- gerou(Y, X), homem(X).
filha(X, Y) :- gerou(Y, X), mulher(X).

avô(X, Y) :- gerou(Z, Y), gerou(X, Z), homem(X).
avó(X, Y) :- gerou(Z, Y), gerou(X, Z), mulher(X).

neto(X, Y) :- gerou(Y, Z), gerou(Z, X), homem(X).
neta(X, Y) :- gerou(Y, Z), gerou(Z, X), mulher(X).

bisavô(X, Y) :- gerou(Z, Y), gerou(W, Z), gerou(X, W), homem(X).
bisavó(X, Y) :- gerou(Z, Y), gerou(W, Z), gerou(X, W), mulher(X).

irmão(X, Y) :- gerou(Z, X), gerou(Z, Y), homem(X), X \== Y.
irmã(X, Y) :- gerou(Z, X), gerou(Z, Y), mulher(X), X \== Y.

tio(X, Y) :- irmão(X, Z), gerou(Z, Y), homem(X).
tia(X, Y) :- irmã(X, Z), gerou(Z, Y), mulher(X).

cunhado(X, Y) :- (casado(X, Z), (irmão(Z, Y); irmã(Z, Y)); ((irmão(X, Z); irmã(X, Z), casado(Z, Y)))), homem(X).
cunhada(X, Y) :- (casado(X, Z), (irmão(Z, Y); irmã(Z, Y)); ((irmão(X, Z); irmã(X, Z), casado(Z, Y)))), mulher(X).

genro(X, Y) :- casado(X, Z), (filho(Z, Y); filha(Z, Y)), homem(X).
nora(X, Y) :- casado(X, Z), (filho(Z, Y); filha(Z, Y)), mulher(X).
