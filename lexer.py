import ply.lex as lex

num_errors = 0

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

# List of token names
tokens = [
    'STRING', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUAL', 'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL',
    'LESS', 'GREATER', 'ASSIGN', 'LPAREN', 'RPAREN',
    'SEMICOLON', 'COMMA', 'TWODOTS', 'LCOMMENT', 'RCOMMENT',
    'PERIOD', 'QUOTATIONMARK', 'LSQUAR', 'RSQUAR', 'LCURLY',
    'RCURLY', 'ARROW', 'COMMENTLINE', 'COLON'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r':='
t_PERIOD = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_QUOTATIONMARK = r'\''
t_NOTEQUAL = r'<>'
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQUAR = r'\['
t_RSQUAR = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_TWODOTS = r'\.\.'
t_ARROW = r'->'
t_LCOMMENT = r'/\*'
t_RCOMMENT = r'\*/'
t_COMMENTLINE = r'//'


# Regular expressions rules
def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'STRING')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    global num_errors
    print("Ilegal character '%s' at line: %d" % (t.value[0], t.lexer.lineno))
    num_errors += 1
    t.lexer.skip(1)


# Building lexer
lexer = lex.lex()

# Test it out
data = '''
 3 + 4 * 10
 + -20 *2
 := 12 () {} what
 packed
 while(true)
 if
 '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
