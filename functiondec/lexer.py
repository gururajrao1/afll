import ply.lex as lex

# List of token names
tokens = (
    'DEF', 'LPAREN', 'RPAREN', 'COLON', 'COMMA', 'EQUAL', 
    'IDENTIFIER', 'FLOAT', 'STRING', 'NUMBER'
)

# Reserved words
reserved = {
    'def': 'DEF',
    'float': 'FLOAT',
    'int': 'INT',
    'str': 'STRING'
}

# Regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_EQUAL = r'='
t_STRING = r'"[^"]*"'  # Matches strings enclosed in double quotes
t_NUMBER = r'\d+(\.\d+)?'  # Matches integers and floats

# Identifier token, checking against reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check if the identifier is a reserved word
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Track line numbers for better error reporting
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Function to tokenize the input string
def tokenize_input(input_string):
    lexer.input(input_string)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    return tokens_list 

# Build the lexer
lexer = lex.lex()

# Example input for testing
input_code = """
def my_function(arg1, arg2):
    x = 10
    y: float = 3.14
    name: str = "Alice"
    pi = 3.14159
"""

# Tokenize the input code
tokens_list = tokenize_input(input_code)

# Print the tokenized output
for token in tokens_list:
    print(token)