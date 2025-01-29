import ply.yacc as yacc
from if_lexer import tokens

class ParserError(Exception):
    pass

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                     | statement NEWLINE statement_list'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[3] if p[1] and p[3] else None

def p_statement(p):
    '''statement : assignment
                | print_statement
                | if_statement
                | standalone_statement'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF expression COLON NEWLINE statement_list
                   | IF expression COLON NEWLINE statement_list NEWLINE elif_block
                   | IF expression COLON NEWLINE statement_list NEWLINE else_block'''
    if p[2] is None:
        raise ParserError("Invalid condition in if statement")
    
    if len(p) == 6:
        p[0] = f"if {p[2]}:\n{p[5]}"
    elif len(p) == 8:
        p[0] = f"if {p[2]}:\n{p[5]}\n{p[7]}"

def p_elif_block(p):
    '''elif_block : ELIF expression COLON NEWLINE statement_list
                 | ELIF expression COLON NEWLINE statement_list NEWLINE elif_block
                 | ELIF expression COLON NEWLINE statement_list NEWLINE else_block'''
    if p[2] is None:
        raise ParserError("Invalid condition in elif statement")
    
    if len(p) == 6:
        p[0] = f"elif {p[2]}:\n{p[5]}"
    else:
        p[0] = f"elif {p[2]}:\n{p[5]}\n{p[7]}"

def p_else_block(p):
    '''else_block : ELSE COLON NEWLINE statement_list'''
    if not hasattr(parser, 'has_if'):
        raise ParserError("'else' without preceding 'if'")
    p[0] = f"else:\n{p[4]}"

def p_expression(p):
    '''expression : IDENTIFIER
                 | NUMBER
                 | comparison_expression'''
    p[0] = p[1]

def p_comparison_expression(p):
    '''comparison_expression : IDENTIFIER EQUALS_EQUALS NUMBER
                           | IDENTIFIER GREATER NUMBER
                           | IDENTIFIER LESSER NUMBER
                           | IDENTIFIER GREATER_EQUALS NUMBER
                           | IDENTIFIER LESSER_EQUALS NUMBER'''
    if not p[1] or not p[3]:
        p[0] = None
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS NUMBER'''
    if not p[1] or not p[3]:
        raise ParserError("Invalid assignment")
    if p[2] == '==':
        raise ParserError("Invalid assignment operator '=='")
    p[0] = f"{p[1]} = {p[3]}"

def p_print_statement(p):
    '''print_statement : PRINT IDENTIFIER'''
    if not p[2]:
        raise ParserError("Invalid print statement")
    p[0] = f"print {p[2]}"

def p_standalone_statement(p):
    '''standalone_statement : IDENTIFIER'''
    p[0] = p[1]

def p_error(p):
    if p:
        error_msg = f"Syntax error at '{p.value}', type '{p.type}'"
    else:
        error_msg = "Syntax error at EOF"
    raise ParserError(error_msg)

parser = yacc.yacc()