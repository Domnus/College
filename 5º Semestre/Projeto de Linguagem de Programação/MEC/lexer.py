#!usr/bin/env python3

import io
import sys
from pathlib import Path

palavrasReservadas = ['if', 'while', 'else', 'int', 'float', 'input', 'print', 'match', 'case', 'import', 'random']
caracteresEspeciais = ['.', ',', '(', ')', '[', ']', '{', '}', '=', '"', "'", ":", ";", "&"]
condicionais = ['%', '!', '?', '<', '>', '+', '-', '*', '/', '=']
condicionaisDuplas = ['!=', '+=', '-=', '*=', '/=', '==', '>=', '<=', '**']

tokens = []


def load_file(file_path):
    with io.open(file_path, mode="r", encoding="utf-8") as file:
        parse_file(file)

    file.close()


def parse_file(file):
    for line in enumerate(file):
        row = line[0]
        text = line[1]

        lex_line(row, text.rstrip())


def lex_line(row, text):
    last_token = ''
    last_dance = ''
    token = ''
    letter = ''
    col = 0

    for col, letter in enumerate(text):
        if letter.isspace():
            if last_token == '':
                pass
        else:
            if last_token + letter in condicionaisDuplas:
                token = last_token + letter
                insert_token(row, col, token, letter)
                token = ''
                last_token = ''
                continue

            if letter in caracteresEspeciais or letter in condicionais:
                if last_token not in caracteresEspeciais:
                    last_token = insert_token(row, col, token, letter)
                    token = ''

            else:
                insert_token(row, col, last_token, letter)
                last_token = ''

            if letter in condicionais:
                last_token = letter
                continue

            if letter.isnumeric():
                if token != '':
                    token += letter
                    continue
                if token.isnumeric():
                    token += letter
                    continue
                insert_token(row, col, token, letter)
                token = ''
                last_dance += letter
                continue
            else:
                if letter == '.':
                    if last_dance:
                        last_dance += letter
                        continue
                    else:
                        insert_token(row, col, last_dance, letter)
                        last_dance = ''
                insert_token(row, col, last_dance, letter)
                last_dance = ''

            if letter in caracteresEspeciais:
                insert_token(row, col, letter, letter)
                token = ''
                last_token = ''
                continue

            else:
                token += letter
                continue

        insert_token(row, col, token, letter)
        token = ''

    insert_token(row, col, token, letter)
    insert_token(row, col, last_token, letter)
    insert_token(row, col, last_dance, letter)


def insert_token(row, col, token, letter):
    if token != '':
        if token in palavrasReservadas:
            tipo = 'Palavra Reservada'
        if token in caracteresEspeciais:
            tipo = 'Caracter Especial'
        elif token in condicionais or token in condicionaisDuplas:
            tipo = 'Condicional'
        elif is_int(token):
            token = int(token)
            tipo = 'Integer'
        elif is_float(token):
            token = float(token)
            tipo = 'Float'
        else:
            tipo = 'String'

        tokens.append((row + 1, (col - len(str(token)) + 1), token, tipo))
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
    file_path = str(Path('exercicio.c').absolute())
    load_file(file_path)
    '''

    # Enable this for regular use
    if len(sys.argv) < 2:
        print("Usa o comando direito seu animal")
        exit(1)

    else:

        subcommand = sys.argv[1]
        file_path = str(Path(subcommand).absolute())

        load_file(file_path)

    return tokens
