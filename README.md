# Automata, Formal Languages, and Logic (AFLL) Project

## 🚀 Overview

This project focuses on **Automata, Formal Languages, and Logic (AFLL)** and includes implementations of a **lexer** and **parser**. The project primarily supports parsing **data types, selection statements, and function declarations**.

## 🎮 Features

- **Lexer Implementation** for tokenizing input.
- **Parser Implementation** for syntactic analysis.
- **Support for Data Types** (e.g., integers, floats, strings).
- **Selection Statements** (if-else, switch-case parsing).
- **Function Declarations** with parameter validation.
- **Error Handling** for incorrect syntax detection.

## 🛠️ Technologies Used

- **Python / C++** – Core language for implementation.


- **Regular Expressions** – Token pattern matching.

## 📜 Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/gururajrao1/afll-project.git
   cd afll-project
   ```
2. Install dependencies (if applicable):
   ```sh
   pip install -r requirements.txt  # For Python
   ```
3. Compile and run the parser:
   ```sh
   make run  # If using a Makefile
   ```

## 🎮 How It Works

1. The **lexer** tokenizes the input source code into meaningful tokens.
2. The **parser** checks if the input follows the defined grammar.
3. It detects **valid and invalid** statements.
4. Outputs **abstract syntax trees (AST)** or error messages.

## 📷 Example Input/Output

**Input:**

```cpp
int main() {
    if (x > 10) {
        return x;
    }
}
```

**Lexer Output:**

```
INT IDENTIFIER '(' ')' '{' IF '(' IDENTIFIER '>' NUMBER ')' '{' RETURN IDENTIFIER ';' '}' '}'
```

**Parser Output:**

```
Valid Syntax!
```

## 🏗️ Future Enhancements

- Support for loops (for, while, do-while).
- Semantic analysis and type checking.
- Code generation for an intermediate representation.

## 🤝 Contributing

Pull requests are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-new-parser-rule`).
3. Commit your changes.
4. Push to your fork and submit a Pull Request

## 📬 Contact



- **Email**: [g](mailto\:your.email@example.com)[uru.raj1207@gmail.com](mailto\:uru.raj1207@gmail.com)

