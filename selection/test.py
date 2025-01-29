from if_lexer import lexer
from if_parser import parser, ParserError

test_code = [
    # Valid cases
    {
        "code": """x = 5
if x == 5:
    print x""",
        "description": "Valid: Basic if with assignment and print",
        "should_pass": True
    },
    

    
    
    
    {
        "code": """if x == 5:
    print x""",
        "description": "Valid: Simple if statement",
        "should_pass": True
    },
    
    # Invalid cases
    {
        "code": """if x == :
    print x""",
        "description": "Invalid: Missing comparison value",
        "should_pass": False
    },
    
    {
        "code": """if x = 5:
    print x""",
        "description": "Invalid: Single = instead of ==",
        "should_pass": False
    },
    
    {
        "code": """if x == 5
    print x""",
        "description": "Invalid: Missing colon after condition",
        "should_pass": False
    },
    
    {
        "code": """else:
    x = 1""",
        "description": "Invalid: else without if",
        "should_pass": False
    }
]

def test_lexer(code):
    print("\nLexical Analysis:")
    print(f"Input code:\n{code}")
    print("\nTokens:")
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
        print(f"Token(type={tok.type}, value={tok.value})")
    return tokens

def test_parser(code):
    print("\nParsing Result:")
    try:
        result = parser.parse(code, debug=True)
        if result is None:
            print("Parsing failed: Invalid syntax")
            return False
        print("Parsing successful")
        return True
    except ParserError as e:
        print(f"Parser Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Lexer and Parser with sample code...")
    print("=" * 60)
    
    success_count = 0
    failure_count = 0
    
    for i, test_case in enumerate(test_code, 1):
        print(f"\nTest Case #{i}: {test_case['description']}")
        print("-" * 40)
        print(f"Expected to {'pass' if test_case['should_pass'] else 'fail'}")
        print("-" * 40)
        
        tokens = test_lexer(test_case['code'])
        parsing_result = test_parser(test_case['code'])
        
        if parsing_result == test_case['should_pass']:
            print("\n✅ Test case behaved as expected")
            success_count += 1
        else:
            print("\n❌ Test case did not behave as expected")
            failure_count += 1
            
        print(f"Expected: {'pass' if test_case['should_pass'] else 'fail'}")
        print(f"Got: {'pass' if parsing_result else 'fail'}")

    print("\n" + "=" * 60)
    print(f"Summary: {success_count} passed, {failure_count} failed")