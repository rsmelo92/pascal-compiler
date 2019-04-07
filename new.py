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
    'repeat': 'REPEAT',
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
    r'\+': 'PLUS',
    r'-': 'MINUS',
    r'\*': 'TIMES',
    r'/': ' DIVIDE',
    r':=': 'ASSIGN',
    r'\.': 'PERIOD',
    r',': 'COMMA',
    r';': 'SEMICOLON',
    r':': 'COLON',
    r'\'': 'QUOTATION_MARK',
    r'<>': 'NOT_EQUAL',
    r'<': 'LESS',
    r'<=': 'LESS_EQUAL',
    r'>': 'GREATER',
    r'>=': 'GREATER_EQUAL',
    r'=': 'EQUAL',
    r'\(': 'LPAREN',
    r'\)': 'RPAREN',
    r'\[': 'LSQUAR',
    r'\]': 'RSQUAR',
    r'\{': 'LCURLY',
    r'\}': 'RCURLY',
    r'\.\.': 'TWO_DOTS',
    r'->': 'ARROW',
    r'/\*': 'LCOMMEN',
    r'\*/': 'RCOMMEN',
    r'//': 'COMMENT_LINE'
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
    print("Linha ", count, "\n", line)
    regex = re.compile(r'[\n\r\t]')
    lineCleaned = regex.sub("", line)

    strings = t_STRING(re.findall("'(.*?)\'", lineCleaned))
    tokens = lineCleaned.split(' ')
    print("Tokens: ", tokens)
    for token in tokens:

        if '\r' in token:
            position = token.find('\r')
            token = token[:position]

        if token in reserved:
            print('reserved: ', reserved[token])

        if token in special_symbols:
            print("special_symbols: ", special_symbols[token])


f.close()
