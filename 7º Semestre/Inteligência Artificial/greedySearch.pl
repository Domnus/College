% REPRESENTAÇÃO DO MAPA %

arc(ara, zerind).
arc(arad, sibiu).
arc(arad, timisoara).

arac(bucharest, fagaras).
arac(bucharest, pitesti).
arac(bucharest, giurgiu).
arac(bucharest, urziceni).

arc(craiova, dobreta).
arc(craiova, rimnicu_vilcea).
arc(craiova, pitest).

arc(dobreta, mahadia).
arc(dobreta, craiova).

arc(efori, hirsova).

arc(fagaras, sibiu).
arc(fagaras, bucharest).

arc(giurgiu, bucharest).

arc(hirsova, urziceni).
arc(hirsova, efori).

arc(iasi, neamt).
arc(iasi, vaslui).

arc(lugoj, timisoara).
arc(lugoj, mehadia).

arc(mehadia, dobreta).
arc(mehadia, lugoj).

arc(neamt, iasi).

arc(oradea, zerind).
arc(oradea, sibiu).

arc(pitesti, rimnicu_vilcea).
arc(pitesti, bucharest).

arc(rimnicu, sibiu).
arc(rimnicu, pitesti).
arc(rimnicu, craiova).

arc(sibiu, arad).
arc(sibiu, fagaras).
arc(sibiu, rimnicu_vilcea).
arc(sibiu, oradea).

arc(timisoara, arad).
arc(timisoara, lugoj).

arc(urziceni, bucharest).
arc(urziceni, hirsova).
arc(urziceni, vaslui).

arc(vaslui, iasi).
arc(vaslui, urziceni).

arc(zerind, arad).
arc(zerind, oradea).

% TABELA DA DISTÂNCIA EURÍSTICA %
h(Node, Value) :- hdist(Node, Value).
h(_, 1).

hdist(arad, 366).
hdist(bucharest, 0).
hdist(craiova, 160).
hdist(dobreta, 242).
hdist(eforie, 161).
hdist(fagaras, 178).
hdist(giurgiu, 77).
hdist(hirsova, 151).
hdist(iasi, 226).
hdist(lugoj, 244).
hdist(mehadia, 241).
hdist(neamt, 234).
hdist(oradea, 380).
hdist(pitesti, 98).
hdist(rimnicu_vilcea, 193).
hdist(sibiu, 253).
hdist(timisoara, 329).
hdist(urziceni, 80).
hdist(vaslui, 199).
hdist(zerind, 374).

% GREEDY SEARCH %

best_first([[Goal|Path]|_], Goal, [Goal|Path], 0).
best_first([Path|Queue], Goal, FinalPath, N) :-
    extend(Path, NewPaths),
    append(Queue, NewPaths, Queue1),
    sort_queue1(Queue1, NewQueue), wrq(NewQueue),
    best_first(NewQueue, Goal, FinalPath, M),
    N is M+1.

extend([Node|Path], NewPaths) :-
    findall([NewNode, Node|Path],
            (arc(Node, NewNode),
             \+ member(NewNode, Path)),
            NewPaths).


sort_queue1(L, L2) :-
    swap1(L, L1), !,
    sort_queue1(L1, L2).
sort_queue1(L, L).

swap1([[A1|B1],[A2|B2]|T], [[A2|B2], [A1|B1]|T]) :-
    hh(A1, W1),
    hh(A2, W2),
    W1>W2.

swap1([X|T], [X|V]) :-
    swap1(T, V).

hh(State, Value) :-
    h(State, Value),
    number(Value), !.

wrq(Q) :- length(Q, N), writeln(N).
