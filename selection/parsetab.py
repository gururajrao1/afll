
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON ELIF ELSE EQUALS EQUALS_EQUALS GREATER GREATER_EQUALS IDENTIFIER IF LESSER LESSER_EQUALS MINUS NEWLINE NUMBER PLUS PRINTprogram : statement_liststatement_list : statement\n| statement NEWLINE statement_liststatement : assignment\n| print_statement\n| if_statement\n| standalone_statementif_statement : IF expression COLON NEWLINE statement_list\n| IF expression COLON NEWLINE statement_list NEWLINE elif_block\n| IF expression COLON NEWLINE statement_list NEWLINE else_blockelif_block : ELIF expression COLON NEWLINE statement_list\n| ELIF expression COLON NEWLINE statement_list NEWLINE elif_block\n| ELIF expression COLON NEWLINE statement_list NEWLINE else_blockelse_block : ELSE COLON NEWLINE statement_listexpression : IDENTIFIER\n| NUMBER\n| comparison_expressioncomparison_expression : IDENTIFIER EQUALS_EQUALS NUMBER\n| IDENTIFIER GREATER NUMBER\n| IDENTIFIER LESSER NUMBER\n| IDENTIFIER GREATER_EQUALS NUMBER\n| IDENTIFIER LESSER_EQUALS NUMBERassignment : IDENTIFIER EQUALS NUMBERprint_statement : PRINT IDENTIFIERstandalone_statement : IDENTIFIER'
    
_lr_action_items = {'IDENTIFIER':([0,9,10,11,26,36,41,42,],[8,13,15,8,8,15,8,8,]),'PRINT':([0,11,26,41,42,],[9,9,9,9,9,]),'IF':([0,11,26,41,42,],[10,10,10,10,10,]),'$end':([1,2,3,4,5,6,7,8,13,18,19,32,34,35,43,44,46,47,],[0,-1,-2,-4,-5,-6,-7,-25,-24,-3,-23,-8,-9,-10,-14,-11,-12,-13,]),'NEWLINE':([3,4,5,6,7,8,13,18,19,20,32,34,35,39,40,43,44,46,47,],[11,-4,-5,-6,-7,-25,-24,-3,-23,26,33,-9,-10,41,42,-14,45,-12,-13,]),'EQUALS':([8,],[12,]),'NUMBER':([10,12,21,22,23,24,25,36,],[16,19,27,28,29,30,31,16,]),'COLON':([14,15,16,17,27,28,29,30,31,37,38,],[20,-15,-16,-17,-18,-19,-20,-21,-22,39,40,]),'EQUALS_EQUALS':([15,],[21,]),'GREATER':([15,],[22,]),'LESSER':([15,],[23,]),'GREATER_EQUALS':([15,],[24,]),'LESSER_EQUALS':([15,],[25,]),'ELIF':([33,45,],[36,36,]),'ELSE':([33,45,],[37,37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,11,26,41,42,],[2,18,32,43,44,]),'statement':([0,11,26,41,42,],[3,3,3,3,3,]),'assignment':([0,11,26,41,42,],[4,4,4,4,4,]),'print_statement':([0,11,26,41,42,],[5,5,5,5,5,]),'if_statement':([0,11,26,41,42,],[6,6,6,6,6,]),'standalone_statement':([0,11,26,41,42,],[7,7,7,7,7,]),'expression':([10,36,],[14,38,]),'comparison_expression':([10,36,],[17,17,]),'elif_block':([33,45,],[34,46,]),'else_block':([33,45,],[35,47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','if_parser.py',8),
  ('statement_list -> statement','statement_list',1,'p_statement_list','if_parser.py',12),
  ('statement_list -> statement NEWLINE statement_list','statement_list',3,'p_statement_list','if_parser.py',13),
  ('statement -> assignment','statement',1,'p_statement','if_parser.py',20),
  ('statement -> print_statement','statement',1,'p_statement','if_parser.py',21),
  ('statement -> if_statement','statement',1,'p_statement','if_parser.py',22),
  ('statement -> standalone_statement','statement',1,'p_statement','if_parser.py',23),
  ('if_statement -> IF expression COLON NEWLINE statement_list','if_statement',5,'p_if_statement','if_parser.py',27),
  ('if_statement -> IF expression COLON NEWLINE statement_list NEWLINE elif_block','if_statement',7,'p_if_statement','if_parser.py',28),
  ('if_statement -> IF expression COLON NEWLINE statement_list NEWLINE else_block','if_statement',7,'p_if_statement','if_parser.py',29),
  ('elif_block -> ELIF expression COLON NEWLINE statement_list','elif_block',5,'p_elif_block','if_parser.py',39),
  ('elif_block -> ELIF expression COLON NEWLINE statement_list NEWLINE elif_block','elif_block',7,'p_elif_block','if_parser.py',40),
  ('elif_block -> ELIF expression COLON NEWLINE statement_list NEWLINE else_block','elif_block',7,'p_elif_block','if_parser.py',41),
  ('else_block -> ELSE COLON NEWLINE statement_list','else_block',4,'p_else_block','if_parser.py',51),
  ('expression -> IDENTIFIER','expression',1,'p_expression','if_parser.py',57),
  ('expression -> NUMBER','expression',1,'p_expression','if_parser.py',58),
  ('expression -> comparison_expression','expression',1,'p_expression','if_parser.py',59),
  ('comparison_expression -> IDENTIFIER EQUALS_EQUALS NUMBER','comparison_expression',3,'p_comparison_expression','if_parser.py',63),
  ('comparison_expression -> IDENTIFIER GREATER NUMBER','comparison_expression',3,'p_comparison_expression','if_parser.py',64),
  ('comparison_expression -> IDENTIFIER LESSER NUMBER','comparison_expression',3,'p_comparison_expression','if_parser.py',65),
  ('comparison_expression -> IDENTIFIER GREATER_EQUALS NUMBER','comparison_expression',3,'p_comparison_expression','if_parser.py',66),
  ('comparison_expression -> IDENTIFIER LESSER_EQUALS NUMBER','comparison_expression',3,'p_comparison_expression','if_parser.py',67),
  ('assignment -> IDENTIFIER EQUALS NUMBER','assignment',3,'p_assignment','if_parser.py',74),
  ('print_statement -> PRINT IDENTIFIER','print_statement',2,'p_print_statement','if_parser.py',82),
  ('standalone_statement -> IDENTIFIER','standalone_statement',1,'p_standalone_statement','if_parser.py',88),
]
