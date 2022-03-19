#!/usr/bin/env python3
from lexer import lexer


tabelaSintatica = {"E": {"id": "TS", "num": "TS", "(" : "TS"},
                   "T": {"id" :"FG", "num" : "FG", "(" : "FG" },
                   "S": {"+" : "+TS", "-" : "-TS", ")": "Vazio", "$": "Vazio"},
                   "G": {"+" : "Vazio", "-" : "Vazio", "*" : "*FG", "/" : "/FG", ")" : "Vazio", "$" : "Vazio"},
                   "F" : {"id" : "id", "num": "num", "(" : "(E)"}
	}

resultado = []

pilha = ["$", "E"]
cadeia = lexer()

for token in cadeia:
	if token[2] in tabelaSintatica[pilha[-1]]:
		regra = (tabelaSintatica["E"][token[2]][::-1])
		pilha.append(regra)

print(pilha)