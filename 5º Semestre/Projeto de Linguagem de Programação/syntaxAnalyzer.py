#!/usr/bin/env python3
from lexer import lexer
import pandas as pd

tabelaSintatica = {
	"E":
		{
			"id" : ["T", "S"], 
			"num": ["T", "S"],
			"("  : ["T", "S"],
			"+"  : "ERRO",
			"-"  : "ERRO",
			"*"  : "ERRO",
			"/"  : "ERRO",
			")"  : "ERRO",
			"$"  : "ERRO"
		},
	"T": 
		{
			"id"  : ["F", "G"],
			"num" : ["F", "G"],
			"("   : ["F", "G"],
			"+"   : "ERRO",
			"-"   : "ERRO",
			"*"   : "ERRO",
			"/"   : "ERRO",
			")"   : "ERRO",
			"$"   : "ERRO"
		},
	"S":
		{
			"+"  : ["+", "T" , "S"],
			"-"  : ["-", "T", "S"],
			")"  : "",
			"$"  : "",
			"id" : "ERRO",
			"num": "ERRO",
			"*"  : "ERRO",
			"/"  : "ERRO",
			"("  : "ERRO",
		},
	"G":
		{
			"+"   : "",
			"-"   : "",
			"*"   : ["*", "F", "G"],
			"/"   : ["/", "F", "G"],
			")"   : "",
			"$"   : "",
			"id"  : "ERRO",
			"num" : "ERRO",
			"("   : "ERRO",
		},
	"F":
		{
			"id"  : "id",
			"num" : "num",
			"("   : ["(", "E", ")"],
			"+"   : "ERRO",
			"-"   : "ERRO",
			"*"   : "ERRO",
			"/"   : "ERRO",
			")"   : "ERRO",
			"$"   : "ERRO"
		}
	}

resultado = {"PILHA" : [],
			 "CADEIA": [],
			 "REGRAS" : []
	}

pilha = ["$", "E"]
cadeia = lexer()
firstIteration = True


def adicionar_na_tabela(pilha, cadeia, regraAtual, tokenResultado, acabou = False):
	pilhaResultado  = ''
	tokensResultado = ''
	regrasResultado = ''

	if len(pilha) == 1 and len(cadeia) == 1:
		if pilha[0] == '$' and cadeia[0][2] == '$':
			resultado["PILHA"].append("$")
			resultado["CADEIA"].append("$")
			resultado["REGRAS"].append("SUCESSO")
	
	else:

		for token in pilha:
			pilhaResultado += token
		resultado["PILHA"].append(pilhaResultado)

		for tokens in cadeia:
			tokensResultado += ' ' + tokens[2]

		resultado["CADEIA"].append(tokensResultado)

		if not acabou:

			if tokenResultado == regraAtual:
				resultado["REGRAS"].append('---')
			else:

				regras = (tabelaSintatica[regraAtual][tokenResultado])

				for regra in regras:
					regrasResultado += regra

				resultado["REGRAS"].append(f"{regraAtual} -> {regrasResultado}")
		else: 
			resultado["REGRAS"].append("Sucesso")


def print_tabela():
	df = pd.DataFrame(resultado).to_string()

	print(df)

while True:
	if len(pilha) == 1 and len(cadeia) == 1:
		if pilha[0] == '$' and cadeia[0][2] == '$':
			adicionar_na_tabela(pilha, cadeia, regraAtual, token[2], True)
			print_tabela()
			break

	else:

		token = cadeia[0]

		if firstIteration:
			regraAtual = pilha[-1]
			firstIteration = False

		else:
			regraAtual = pilha[-1]

		adicionar_na_tabela(pilha, cadeia, regraAtual, token[2])

		if pilha[-1] == token[2]:
			pilha.pop()
			cadeia.pop(0)

		else:
			regraAtual = pilha.pop()
			if token[2] in tabelaSintatica[regraAtual]:
				regras = (tabelaSintatica[regraAtual][token[2]])

				if regras == "ERRO":
					print("ERRO")
					print(f"Token inválido: {token[2]} em {token[0]}:{token[1]}")
					break

				if regras == '':
					continue

				elif type(regras) == str: 
					pilha.append(regras)

				else:
					[pilha.append(regra) for regra in regras[::-1]]
