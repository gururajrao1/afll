from parser import parser
from lexer import *

# Example function declarations
test_code = [
    "def my_function(arg1, arg2:",                    # Valid
              
    # "def another_function():",                         # Valid with no parameters
    
]

for code in test_code:
    print(f"Testing: {code}")
    parser.parse(code)
    print("\n--- TOKENIZING ---")
    tokens = tokenize_input(code)
    for tok in tokens:
        print(f"Token(type={tok.type}, value={tok.value})")
    print("\n--- VALIDITY CHECK ---")
    print()
