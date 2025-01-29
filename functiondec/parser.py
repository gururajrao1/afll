import ply.yacc as yacc
from lexer import tokens

# Parsing rules
def p_function_declaration(p):
    '''function_declaration : DEF IDENTIFIER LPAREN parameter_list RPAREN COLON'''
    print(f"Function '{p[2]}' declaration is syntactically correct.")

def p_parameter_list(p):
    '''parameter_list : parameters
                      | empty'''
    pass

def p_parameters(p):
    '''parameters : parameter
                  | parameter COMMA parameters_without_default
                  | parameter_with_default'''
    pass

def p_parameters_without_default(p):
    '''parameters_without_default : parameter
                                  | parameter COMMA parameters_without_default'''
    pass

def p_parameter(p):
    '''parameter : IDENTIFIER'''
    pass

def p_parameter_with_default(p):
    '''parameter_with_default : parameter EQUAL IDENTIFIER
                              | parameter EQUAL NUMBER
                              | parameter EQUAL STRING'''
    pass

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

'''
### Context-Free Grammar (CFG)

S → function_declaration

function_declaration → DEF IDENTIFIER LPAREN parameter_list RPAREN COLON

parameter_list → parameters | empty

parameters → parameter
parameters → parameter COMMA parameters_without_default
parameters → parameter_with_default

parameters_without_default → parameter
parameters_without_default → parameter COMMA parameters_without_default

parameter → IDENTIFIER
parameter_with_default → parameter EQUAL IDENTIFIER
parameter_with_default → parameter EQUAL NUMBER
parameter_with_default → parameter EQUAL STRING

empty →
'''
