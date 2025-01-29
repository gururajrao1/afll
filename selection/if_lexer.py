import ply.lex as lex

# List of token names
tokens = (
    'IF', 'ELIF', 'ELSE',
    'PRINT',
    'IDENTIFIER', 'NUMBER',
    'EQUALS', 'COLON', 'NEWLINE',
    'GREATER', 'LESSER', 'GREATER_EQUALS', 'LESSER_EQUALS', 'EQUALS_EQUALS',
    'PLUS', 'MINUS'
)

# Regular expressions for simple tokens
t_EQUALS = r'='
t_EQUALS_EQUALS = r'=='
t_COLON = r':'
t_GREATER = r'>'
t_LESSER = r'<'
t_GREATER_EQUALS = r'>='
t_LESSER_EQUALS = r'<='
t_PLUS = r'\+'
t_MINUS = r'-'
t_ignore = ' \t'  # Ignore spaces and tabs

# Regular expressions for keywords
def t_IF(t):
    r'if'
    return t

def t_ELIF(t):
    r'elif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

# Regular expression for identifiers (variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check if it's not a keyword
    if t.value in {'if', 'elif', 'else', 'print'}:
        t.type = t.value.upper()
    return t

# Regular expression for numbers (integers)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Handle newlines for line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()