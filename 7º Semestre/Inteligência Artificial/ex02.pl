% Josevaldo nasceu em Marília
% Karina nasceu em Milão
% Marília fica no estado de São Paulo
% Milão fica na Itália
% Só é Paulista quem nasce em São Paulo

% Fatos %
nasceu(josevaldo, marilia).
nasceu(karina, milao).

fica(marilia, saopaulo).
fica(milao, italia).

% Regras %
paulista(X) :- nasceu(X, Y), fica(Y, saopaulo).
