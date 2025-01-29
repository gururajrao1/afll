from lexer import tokenize_input
from parser import parser, ParserError

test_code = [
    # Valid cases
    {
        "code": "x",
        "description": "Valid: Simple variable reference",
        "should_pass": True
    },
    {
        "code": "y: double = 3.142",
        "description": "Valid: Variable declaration with type and float value",
        "should_pass": True
    },
    {
        "code": "z = 42",
        "description": "Valid: Variable assignment with integer",
        "should_pass": True
    },
    {
        "code": "a: int",
        "description": "Valid: Variable declaration with type only",
        "should_pass": True
    },
    {
        "code": "b = int(4.7)",
        "description": "Valid: Variable assignment with type conversion",
        "should_pass": True
    },
    {
        "code": 'name: str = "gururaj"',
        "description": "Valid: String variable with type declaration",
        "should_pass": True
    },
    {
        "code": "pi: float = 3.14",
        "description": "Valid: Float variable with type declaration",
        "should_pass": True
    },
    {
        "code": "c = str(123)",
        "description": "Valid: String conversion assignment",
        "should_pass": True
    },
    # Invalid cases
    {
        "code": "@invalid",
        "description": "Invalid: Special character in identifier",
        "should_pass": False
    },
    {
        "code": "x = ",
        "description": "Invalid: Missing value after equals",
        "should_pass": False
    },
    {
        "code": ": int",
        "description": "Invalid: Missing identifier before type",
        "should_pass": False
    },
    {
        "code": "x: invalid_type",
        "description": "Invalid: Unknown type",
        "should_pass": False
    }
]

def run_tests():
    print("Testing Lexer and Parser with sample code...")
    print("=" * 60)
    
    success_count = 0
    failure_count = 0
    
    for i, test_case in enumerate(test_code, 1):
        print(f"\nTest Case #{i}: {test_case['description']}")
        print("-" * 40)
        print(f"Expected to {'pass' if test_case['should_pass'] else 'fail'}")
        print("-" * 40)
        
        code = test_case['code']
        print(f"\nTesting: {code}")
        
        test_passed = True
        tokens = None
        
        print("\n--- TOKENIZING ---")
        try:
            tokens = tokenize_input(code)
            for tok in tokens:
                print(f"Token(type={tok.type}, value={tok.value})")
        except Exception as e:
            print(f"Tokenizing error: {str(e)}")
            test_passed = False
            
        print("\n--- PARSING ---")
        if test_passed:  # Only try parsing if tokenizing succeeded
            try:
                result = parser.parse(code)
                if result is None:
                    print("Parsing failed: No result")
                    test_passed = False
                else:
                    print(f"Result: {result}")
            except (ParserError, SyntaxError) as e:
                print(f"Parsing error: {str(e)}")
                test_passed = False
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                test_passed = False
            
        if test_passed == test_case['should_pass']:
            print("\n✅ Test case behaved as expected")
            success_count += 1
        else:
            print("\n❌ Test case did not behave as expected")
            failure_count += 1
            
        print(f"Expected: {'pass' if test_case['should_pass'] else 'fail'}")
        print(f"Got: {'pass' if test_passed else 'fail'}")
        
    print("\n" + "=" * 60)
    print(f"Summary: {success_count} passed, {failure_count} failed")

if __name__ == "__main__":
    run_tests()