import ply.lex as lex

# Token list
tokens = (
    'INT', 'FLOAT', 'STRING_TYPE', 'DOUBLE',
    'IDENTIFIER', 'NUMBER', 'STRING',
    'EQUAL', 'COLON', 'LPAREN', 'RPAREN'
)

# Regular expressions for tokens
t_EQUAL = r'='
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Keywords
def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_STRING_TYPE(t):
    r'str'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d*\.?\d+'
    try:
        t.value = float(t.value) if '.' in t.value else int(t.value)
        return t
    except ValueError:
        raise ValueError(f"Invalid number format: {t.value}")

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling
def t_error(t):
    raise ValueError(f"Illegal character '{t.value[0]}'")

# New line handling
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

def tokenize_input(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens