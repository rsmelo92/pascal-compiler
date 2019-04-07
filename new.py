import re

f = open('pascal.pas', 'r')

reserved = {
    'and': 'AND',
    'array': 'ARRAY',
    'begin': 'BEGIN',
    'case': 'CASE',
    'char': 'CHAR',
    'const': 'CONST',
    'div': 'DIV',
    'do': 'DO',
    'downto': 'DOWNTO',
    'else': 'ELSE',
    'end': 'END',
    'file': 'FILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'goto': 'GOTO',
    'if': 'IF',
    'in': 'IN',
    'integer': 'INTEGER',
    'label': 'LABEL',
    'mod': 'MOD',
    'nil': 'NIL',
    'not': 'NOT',
    'of': 'OF',
    'or': 'OR',
    'packed': 'PACKED',
    'procedure': 'PROCEDURE',
    'program': 'PROGRAM',
    'real': 'REAL',
    'repeat': 'REPEAT',
    'record': 'RECORD',
    'set': 'SET',
    'then': 'THEN',
    'to': 'TO',
    'type': 'TYPE',
    'until': 'UNTIL',
    'while': 'WHILE',
    'var': 'VAR',
    'with': 'WITH',
}

special_symbols = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'TIMES',
    '/': ' DIVIDE',
    ':=': 'ASSIGN',
    '.': 'PERIOD',
    ',': 'COMMA',
    ';': 'SEMICOLON',
    ':': 'COLON',
    "'": 'QUOTATION_MARK',
    '<>': 'NOT_EQUAL',
    '<': 'LESS',
    '<=': 'LESS_EQUAL',
    '>': 'GREATER',
    '>=': 'GREATER_EQUAL',
    '=': 'EQUAL',
    '(': 'LPAREN',
    ')': 'RPAREN',
    '[': 'LSQUAR',
    ']': 'RSQUAR',
    '{': 'LCURLY',
    '}': 'RCURLY',
    '..': 'TWO_DOTS',
    '->': 'ARROW',
    '\*': 'LCOMMEN',
    '*/': 'RCOMMEN',
    '//': 'COMMENT_LINE'
}


i = f.read()


count = 0
program = i.split('\n')


def t_STRING(t):
    if t:
        if t[0] in reserved:
            print('reserved: ', reserved[t])
        else:
            print('STRING: ', t[0])
        return t
    return []


for line in program:
    count = count+1
    print('\n')
    print("Linha ", count, "\n", line, "\n")

    removeBreaks = re.compile(r'[\n\r\t]')
    lineCleaned = removeBreaks.sub("", line)

    strings = t_STRING(re.findall("'(.*?)\'", lineCleaned))

    tokens = lineCleaned.split(' ')
    print("Tokens: ", tokens)

    for token in tokens:
        if '\r' in token:
            position = token.find('\r')
            token = token[:position]

        if token in reserved:
            print('reserved: ', reserved[token])
            print(True)

        if token in special_symbols:
            print("special_symbols: ", special_symbols[token])
            print(True)

f.close()
