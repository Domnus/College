% Sócrates é Homem
% Todo Homem é Mortal
% Logo, Sócrates é Mortal


% Fatos

homem(socrates).
solteiro(hanai).

% Regras %

mortal(X) :- homem(X).
