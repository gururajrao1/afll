
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DEF EQUAL FLOAT IDENTIFIER LPAREN NUMBER RPAREN STRINGfunction_declaration : DEF IDENTIFIER LPAREN parameter_list RPAREN COLONparameter_list : parameters\n| emptyparameters : parameter\n| parameter COMMA parameters_without_default\n| parameter_with_defaultparameters_without_default : parameter\n| parameter COMMA parameters_without_defaultparameter : IDENTIFIERparameter_with_default : parameter EQUAL IDENTIFIER\n| parameter EQUAL NUMBER\n| parameter EQUAL STRINGempty :'
    
_lr_action_items = {'DEF':([0,],[2,]),'$end':([1,14,],[0,-1,]),'IDENTIFIER':([2,4,12,13,20,],[3,5,5,17,5,]),'LPAREN':([3,],[4,]),'RPAREN':([4,5,6,7,8,9,10,15,16,17,18,19,21,],[-13,-9,11,-2,-3,-4,-6,-7,-5,-10,-11,-12,-8,]),'COMMA':([5,9,15,],[-9,12,20,]),'EQUAL':([5,9,],[-9,13,]),'COLON':([11,],[14,]),'NUMBER':([13,],[18,]),'STRING':([13,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function_declaration':([0,],[1,]),'parameter_list':([4,],[6,]),'parameters':([4,],[7,]),'empty':([4,],[8,]),'parameter':([4,12,20,],[9,15,15,]),'parameter_with_default':([4,],[10,]),'parameters_without_default':([12,20,],[16,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> function_declaration","S'",1,None,None,None),
  ('function_declaration -> DEF IDENTIFIER LPAREN parameter_list RPAREN COLON','function_declaration',6,'p_function_declaration','parser.py',6),
  ('parameter_list -> parameters','parameter_list',1,'p_parameter_list','parser.py',10),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','parser.py',11),
  ('parameters -> parameter','parameters',1,'p_parameters','parser.py',15),
  ('parameters -> parameter COMMA parameters_without_default','parameters',3,'p_parameters','parser.py',16),
  ('parameters -> parameter_with_default','parameters',1,'p_parameters','parser.py',17),
  ('parameters_without_default -> parameter','parameters_without_default',1,'p_parameters_without_default','parser.py',21),
  ('parameters_without_default -> parameter COMMA parameters_without_default','parameters_without_default',3,'p_parameters_without_default','parser.py',22),
  ('parameter -> IDENTIFIER','parameter',1,'p_parameter','parser.py',26),
  ('parameter_with_default -> parameter EQUAL IDENTIFIER','parameter_with_default',3,'p_parameter_with_default','parser.py',30),
  ('parameter_with_default -> parameter EQUAL NUMBER','parameter_with_default',3,'p_parameter_with_default','parser.py',31),
  ('parameter_with_default -> parameter EQUAL STRING','parameter_with_default',3,'p_parameter_with_default','parser.py',32),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',36),
]
