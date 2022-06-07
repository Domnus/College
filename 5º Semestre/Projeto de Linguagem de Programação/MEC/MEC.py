from lexer import lexer

condicionais = ['%', '!', '?', '<', '>', '+', '-', '*', '/', '=', '!=', '+=', '-=', '*=', '/=', '==', '>=', '<=', '**']

cVerificador = 0
armazenar = ''
condicional = ''

global jump
jump = 0

erros = []

result = open('resultado.mec', 'w')

# set of operators
OPERATORS = {'+', '-', '*', '/', '(', ')', '>', '>=', '<', '<=', '!=', '==', '&&', '||'}
# dictionary having priorities
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '>': 3, '>=': 3, '<': 3, '<=': 3, '!=': 3, '==': 3, '&&': 4, '||': 5}


def infix_to_postfix(expression):
    stack = []
    output = []

    for ch in expression:
        if ch not in OPERATORS:
            output.append(ch)

        elif ch == '(':
            stack.append('(')

        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return output


def insert_expression(expressao, variaveis):
    for token in expressao:
        if token in variaveis:
            insert(True, 'CRVL ' + token)
        elif token in OPERATORS:
            match token:
                case "<":
                    insert(True, 'CMME')
                case ">":
                    insert(True, 'CMMA')
                case "==":
                    insert(True, 'CMIG')
                case "!=":
                    insert(True, "CMDG")
                case "<=":
                    insert(True, 'CMEG')
                case ">=":
                    insert(True, 'CMAG')
                case "+":
                    insert(True, 'SOMA')
                case "-":
                    insert(True, 'SUIT')
                case "*":
                    insert(True, 'MULT')
                case "/":
                    insert(True, 'DIVI')
        else:
            insert(True, 'CRCT ' + str(token))


def insert(tab, instrucao):
    if tab:
        result.write('\t')
    result.write(instrucao)
    result.write('\n')

def get_variable_count(cadeia):
    contando = False
    variaveis = []

    for tokenAtual in cadeia:
        if tokenAtual == "int":
            contando = True
            continue

        if contando:
            if tokenAtual == ',':
                continue
            elif tokenAtual == ';':
                contando = False
            else:
                variaveis.append(tokenAtual)

    return variaveis


def check_scope(token, contador, _pilha):
    if token in ['(', '{']:
        contador += 1
    if token in [')', '}']:
        contador -= 1

    _pilha.append(token)

    return contador, _pilha


def enquanto_function(stack, variaveis, jump):
    while_condicao = False
    expressao = []
    _pilha = []

    for token in stack:
        match token:
            case '(':
                while_condicao = True
                continue
            case ')':
                while_condicao = False
                insert_expression(infix_to_postfix(expressao), variaveis)
                expressao = []

                insert(True, 'DSVF L' + str(jump))
                index = stack.index(token) + 1
                break

        if while_condicao:
            expressao.append(token)

    _pilha = stack[index::]

    mec(_pilha, variaveis)


    insert(True, 'DSVS L' + str(jump - 1))
    insert(False, 'L' + str(jump) + '\tWHILE')


def se_function(stack, variaveis, index, jump):
    if_condicao = False
    expressao = []

    for token in stack:
        match token:
            case '(':
                if_condicao = True
                continue
            case ')':
                if_condicao = False
                insert_expression(infix_to_postfix(expressao), variaveis)
                expressao = []

                insert(True, 'DSVF L' + str(jump))
                index = stack.index(token) + 1
                continue

        if if_condicao:
            expressao.append(token)
            continue

    _pilha = stack[index::]

    mec(_pilha, variaveis)

    if stack[-1] == "else":
        insert(True, 'DSVS L' + str(jump + 1))

    insert(False, 'L' + str(jump) + '\tIF')


def senao_function(stack, variaveis, jump):
    mec(stack, variaveis)
    insert(False, 'L' + str(jump + 1) + '\tELSE')


def mec(cadeia, variaveis):
    global jump
    expr = []
    pilha = []

    cont = 0

    enquanto = False
    se = False
    senao = False

    lendo = False
    ler = False
    atribuir = False
    imprimir = False

    for i in range(len(cadeia)):
        tokenAtual = cadeia[i]

        match tokenAtual:
            case 'main':
                insert(True, 'INPP')
                insert(True, 'AMEM ' + str(len(variaveis)))
            case 'scanf':
                if not enquanto and not se and not senao:
                    insert(True, 'LEIT')
                    lendo = True
            case 'while':
                if not se and not senao:
                    enquanto = True
                    insert(False, 'L' + str(jump) + '\tWHILE')
                    jump += 1
                    continue
            case 'printf':
                if not enquanto and not se and not senao:
                    imprimir = True
            case 'if':
                if not enquanto and not senao:
                    se = True
                    jump += 1
                    continue
            case 'else':
                if not enquanto and not se:
                    senao = True
                    continue

        if lendo and tokenAtual == '&':
            ler = True
            continue

        if ler:
            insert(True, 'ARMZ ' + tokenAtual)
            ler = False
            lendo = False

        if tokenAtual in variaveis and not atribuir:
            armazenar = tokenAtual

        if tokenAtual == '=' and not enquanto and not se:
            atribuir = True
            continue

        if atribuir:
            if tokenAtual != ';':
                expr.append(tokenAtual)
                continue
            else:
                insert_expression(infix_to_postfix(expr), variaveis)
                expr = []

            insert(True, 'ARMZ ' + armazenar)
            armazenar = ''

            atribuir = False
            continue

        if imprimir:
            if tokenAtual in variaveis:
                insert(True, 'CRVL ' + tokenAtual)
                insert(True, 'IMPR')
                imprimir = False

        if enquanto:
            cont, pilha = check_scope(tokenAtual, cont, pilha)
            if cont == 0 and tokenAtual == '}':
                enquanto_function(pilha, variaveis, jump)
                pilha = []
                enquanto = False
            continue

        if se:
            cont, pilha = check_scope(tokenAtual, cont, pilha)

            if cont == 0 and tokenAtual == '}':
                if "else" in cadeia:
                    pilha.append("else")
                se_function(pilha, variaveis, i, jump)
                pilha = []
                se = False
            continue

        if senao:
            cont, pilha = check_scope(tokenAtual, cont, pilha)
            if cont == 0 and tokenAtual == '}':
                senao_function(pilha, variaveis, jump)
                pilha = []
                senao = False
            continue


input = []
cadeia = lexer()

for i in range(len(cadeia)):
    input.append(cadeia[i][2])

variaveis = get_variable_count(input)
mec(input, variaveis)

insert(True, 'DMEM ' + str(len(variaveis)))
insert(True, 'PARA')

if cVerificador % 2 != 0:
    erros.append("Erro de sintaxe")

if len(erros) > 0:
    for erro in erros:
        print(erro)
    exit(1)

result.close()


