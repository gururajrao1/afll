import ply.yacc as yacc
from lexer import tokens

class ParserError(Exception):
    pass

# Parsing rules
def p_statement(p):
    '''statement : declaration
                | assignment
                | type_declaration'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : type IDENTIFIER EQUAL expression
                  | type IDENTIFIER COLON expression
                  | IDENTIFIER COLON type
                  | IDENTIFIER EQUAL type LPAREN expression RPAREN
                  | IDENTIFIER'''

    # Case: Simple variable declaration (x)
    if len(p) == 2:
        p[0] = f"Declared variable '{p[1]}' with no initial value."
    
    # Case: Type hint only (x: int)
    elif len(p) == 4 and p[2] == ':':
        p[0] = f"Declared variable '{p[1]}' with type hint '{p[3]}' and no initial value."
    
    # Case: Type with direct value (int x = 5)
    elif len(p) == 5 and p[3] == '=':
        p[0] = f"Declared variable '{p[2]}' with initial value '{p[4]}'."
    
    # Case: Type with colon value (int x: 5)
    elif len(p) == 5 and p[3] == ':':
        p[0] = f"Declared variable '{p[2]}' with initial value '{p[4]}'."
    
    # Case: Type casting (x = int(4.7))
    elif len(p) == 7:
        p[0] = f"Declared variable '{p[1]}' with initial value '{p[5]}', cast to type '{p[3]}'."

def p_type_declaration(p):
    '''type_declaration : IDENTIFIER COLON type EQUAL expression'''
    p[0] = f"Declared variable '{p[1]}' of type '{p[3]}' with initial value '{p[5]}'."

def p_assignment(p):
    '''assignment : IDENTIFIER EQUAL expression'''
    p[0] = f"Assigned value '{p[3]}' to variable '{p[1]}'."

def p_type(p):
    '''type : INT
            | FLOAT
            | STRING_TYPE
            | DOUBLE'''
    p[0] = p[1]

def p_expression(p):
    '''expression : NUMBER
                 | STRING
                 | type LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        p[0] = f"{p[1]}({p[3]})"

# Error rule for syntax errors
def p_error(p):
    if p:
        raise ParserError(f"Syntax error at '{p.value}'")
    else:
        raise ParserError("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()