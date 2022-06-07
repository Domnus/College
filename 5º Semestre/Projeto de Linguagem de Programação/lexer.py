#!usr/bin/env python3

import io
import sys
from pathlib import Path

#palavrasReservadas = ['if','while','else','int','float','input','print','match','case','import','random']
caracteresEspeciais = ['.', ',', '(', ')', '[', ']', '{', '}', '=', '\"', "\'", ":",";"]
condicionais = ['%','!','?','<','>', '+', '-', '*', '/', '=']
condicionaisDuplas = ['!=','+=', '-=', '*=', '/=','==','>=','<=', '**']

tokens = []


def load_file(filePath):
    with io.open(filePath, mode="r", encoding="utf-8") as file:
        parse_file(file)

    file.close()


def parse_file(file):
    for line in enumerate(file):
        row  = line[0]
        text = line[1]
        
        lex_line(row, text.rstrip())


def lex_line(row, text):
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
                insert_token(row, col, token, letter)
                token = ''
                lastToken = ''
                continue
            else:
                insert_token(row, col, lastToken, letter)
                lastToken = ''

            if letter in condicionais:
                lastToken = letter
                continue

            if letter.isnumeric():
                if token:
                    token += letter
                    continue
                insert_token(row, col, token, letter)
                token = ''
                lastDance += letter
                continue
            else:
                if letter == '.':
                    if lastDance:
                        lastDance += letter
                        continue
                    else: 
                        insert_token(row, col, lastDance, letter)
                        lastDance= ''
                insert_token(row, col, lastDance, letter)
                lastDance= ''
                
            #if letter in palavrasReservadas or letter in caracteresEspeciais:
            if letter in caracteresEspeciais:
                token = insert_token(row, col, token, letter)
            else:
                token += letter
                continue

        insert_token(row, col, token, letter)
        token = ''
    token = insert_token(row, col, token, letter)
    insert_token(row, col, lastToken, letter)
    insert_token(row, col, lastDance, letter)


def insert_token(row, col, token, letter):
    if token != '':
#        if token in palavrasReservadas:
#            taipe = 'Palavra Reservada'
        if token in caracteresEspeciais:
            taipe = 'Caracter Especial'
        elif token in condicionais or token in condicionaisDuplas:
            taipe = 'Condicional'
        elif is_int(token):
            token = int(token)
            taipe = 'Integer'
        elif is_float(token):
            token = float(token)
            taipe = 'Float'
        else:
            taipe = 'String'
        
        tokens.append((row + 1, (col - len(str(token)) + 1), token, taipe))
    return letter


def is_int(token):
    try:
        token = int(token)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_float(token):
    try:
        token = float(token)
    except (TypeError, ValueError):
        return False
    else:
        return True


def lexer():
    # Enable this for debug
    '''
    filePath = str(Path('teste.txt').absolute())
    load_file(filePath)
    '''

    #Enable this for regular use
    if len(sys.argv) < 2:
        print("Usa o comando direito seu animal")
        exit(1)

    else:

        subcommand = sys.argv[1]
        filePath = str(Path(subcommand).absolute())

        load_file(filePath)

    return tokens
