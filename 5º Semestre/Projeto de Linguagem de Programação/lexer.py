#!usr/bin/env python3

import io
import sys
from pathlib import Path

#palavrasReservadas = ['if','while','else','int','float','input','print','match','case','import','random']
caracteresEspeciais = ['.', ',', '(', ')', '[', ']', '{', '}', '=', '\"', "\'", ":",";"]
condicionais = ['%','!','?','<','>', '+', '-', '*', '/', '=']
condicionaisDuplas = ['!=','+=', '-=', '*=', '/=','==','>=','<=', '**']

tokens = []


def loadFile(filePath):
    with io.open(filePath, mode="r", encoding="utf-8") as file:
        parseFile(file)

    file.close()


def parseFile(file):
    for line in enumerate(file):
        row  = line[0]
        text = line[1]
        
        lexLine(row, text.rstrip())


def lexLine(row, text):
    lastToken  = ''
    lastDance= ''
    token  = ''
    letter = ''
    col = 0

    for col, letter in enumerate(text):
        if letter.isspace():
            if lastToken == '':
                pass
        else:
            if lastToken + letter in condicionaisDuplas:
                token = lastToken + letter
                insertToken(row, col, token, letter)
                token = ''
                lastToken = ''
                continue
            else:
                insertToken(row, col, lastToken, letter)
                lastToken = ''

            if letter in condicionais:
                lastToken = letter
                continue

            if letter.isnumeric():
                if token:
                    token += letter
                    continue
                insertToken(row, col, token, letter)
                token = ''
                lastDance += letter
                continue
            else:
                if letter == '.':
                    if lastDance:
                        lastDance += letter
                        continue
                    else: 
                        insertToken(row, col, lastDance, letter)
                        lastDance= ''
                insertToken(row, col, lastDance, letter)
                lastDance= ''
                
            #if letter in palavrasReservadas or letter in caracteresEspeciais:
            if letter in caracteresEspeciais:
                token = insertToken(row, col, token, letter)
            else:
                token += letter
                continue

        insertToken(row, col, token, letter)
        token = ''
    token = insertToken(row, col, token, letter)
    insertToken(row, col, lastToken, letter)
    insertToken(row, col, lastDance, letter)


def insertToken(row, col, token, letter):
    if token != '':
#        if token in palavrasReservadas:
#            taipe = 'Palavra Reservada'
        if token in caracteresEspeciais:
            taipe = 'Caracter Especial'
        elif token in condicionais or token in condicionaisDuplas:
            taipe = 'Condicional'
        elif isint(token):
            token = int(token)
            taipe = 'Integer'
        elif isfloat(token):
            token = float(token)
            taipe = 'Float'
        else:
            taipe = 'String'
        
        tokens.append((row + 1, (col - len(str(token)) + 1), token, taipe))
    return letter


def isint(token):
    try:
        token = int(token)
    except (TypeError, ValueError):
        return False
    else:
        return True


def isfloat(token):
    try:
        token = float(token)
    except (TypeError, ValueError):
        return False
    else:
        return True


def lexer():
    # Enable this for debug
    filePath = str(Path('teste.txt').absolute())

    loadFile(filePath)
    for token in tokens:
        print(token)
    '''

    #Enable this for regular use
    if len(sys.argv) < 2:
        print("Usa o comando direito seu animal")
        exit(1)

    else:

        subcommand = sys.argv[1]
        filePath = str(Path(subcommand).absolute())

        loadFile(filePath)

    '''

    return tokens
