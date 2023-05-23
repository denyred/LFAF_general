# Parser & Building an Abstract Syntax Tree
## Course: Formal Languages & Finite Automata
## Author: Spataru Dionisie FAF-211


## Theory
Parsing is the process of analyzing a sequence of symbols according to the rules of a formal grammar. It is used to determine the structure and meaning of the input. In programming, parsing is commonly used for tasks like interpreting programming languages, processing markup languages, or extracting information from structured data.

There are two main approaches to parsing:

Top-down Parsing: It starts from the root of the parse tree and expands non-terminal symbols to match the input. Recursive Descent and LL(k) parsing are popular top-down parsing algorithms.
Bottom-up Parsing: It starts from the input symbols and constructs the parse tree by reducing a sequence of input symbols to non-terminal symbols. Shift-Reduce and LR(k) parsing are commonly used bottom-up parsing techniques.
Additional parsing techniques include Earley parsing, which handles a broader class of grammars, and CYK parsing, which works with grammars in Chomsky normal form.

Parsing is implemented by representing the grammar using formal notations like BNF or EBNF. There are various tools and libraries available for programming parsing, such as Lex/Yacc, ANTLR, PLY, and parser combinator libraries like Parsec or Sprache. These tools simplify the process of parsing and language processing in software development.

### Abstract Syntax Tree (AST):

Introduction:
-An Abstract Syntax Tree (AST) is a hierarchical representation of the structure and semantics of a program or a piece of code.
-ASTs are commonly used in programming language theory, compilers, interpreters, and static analysis tools.
Structure and Purpose:
-ASTs capture the essential elements of the program's syntax while abstracting away details like punctuation and formatting.
-Each node in the AST represents a specific construct or operation in the code, such as statements, expressions, or declarations.
-The hierarchical structure of the AST reflects the nesting and relationships between these constructs.
Construction of AST:
-ASTs are typically generated during the parsing phase of compilation or interpretation.
-During parsing, the input code is transformed into a parse tree, which is then transformed into an AST by discarding unnecessary details.
-The AST construction process involves recognizing the grammar rules and mapping them to appropriate AST node types.
AST Node Types:
-AST nodes represent different language constructs, such as loops, conditionals, function definitions, variable declarations, and expressions.
-Each node type has associated properties and children nodes that carry additional information and capture the relationships between constructs.
Benefits of ASTs:
-ASTs provide a higher-level representation of the program, making it easier to analyze and manipulate.
-ASTs facilitate semantic analysis, optimization, and code transformations during compilation or interpretation.
-ASTs enable the extraction of information and the generation of documentation or code refactoring tools.
AST Traversal:
-Traversing an AST involves visiting nodes in a specific order to perform operations like type checking, code generation, or static analysis.
-Common traversal algorithms include depth-first traversal (pre-order, post-order) and breadth-first traversal.
Visualization and Debugging:
-ASTs can be visualized graphically to aid understanding and debugging.
-Tools like graphviz or tree visualization libraries can generate visual representations of ASTs for better visualization and analysis.
Overall, ASTs play a vital role in language processing and analysis, providing a structured representation of code that facilitates various compiler and interpreter tasks, as well as static analysis and tool development.

## Objectives

1. Get familiar with parsing, what it is and how it can be programmed.
2. Get familiar with the concept of AST.
3. In addition to what has been done in the 3rd lab work do the following:
- In case you didn't have a type that denotes the possible types of tokens you need to:
a. Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
b. Please use regular expressions to identify the type of the token.
4. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
5. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description

### TokenType

As per 3rd objective is requested to have a  TokenType that can be used in the lexical analysis to categorize the tokens.
I already have this type of implementation.

When the tokenize method of the Lexer class is invoked, it proceeds to iterate over these defined patterns. During each iteration, it attempts to match the patterns against the input string. If a match is found, indicating the presence of a token, the Lexer records the token's type and value and adds it to a list of tokens.

Additionally, the Lexer class incorporates error handling capabilities. If an invalid character is encountered during the tokenization process, the class raises an exception, specifically an Invalid Character exception, to alert the user of the unrecognized input.

The Lexer class acts as a fundamental component in the process of language processing. It serves as the initial stage in parsing and interpreting code by breaking down the input string into meaningful tokens. These tokens can then be utilized by subsequent stages, such as the parser or interpreter, to understand and manipulate the code effectively.
```python
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token(type='{self.type}', value={self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token('INTEGER', self.integer())

            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return Token('MUL', '*')

            if self.current_char == '/':
                self.advance()
                return Token('DIV', '/')

            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')

            if self.current_char.isalpha():
                return Token('ID', self.current_char)

            raise Exception(f"Invalid character: {self.current_char}")

        return Token('EOF', None)
```
In summary, the token class plays a vital role in the lexer's workflow, allowing the identification and organization of lexemes into meaningful categories. These tokens serve as intermediaries, conveying important information about the lexemes to subsequent stages of language processing, ultimately aiding in the comprehensive analysis and interpretation of the input source code.


### Class AST
```python
    class AST:
    def __init__(self, value=None, left=None, operator=None, right=None):
        self.value = value
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        if self.value is not None:
            return f"AST(value={self.value})"
        return f"AST(left={self.left}, operator={self.operator}, right={self.right})"
```
class AST: This class represents a node in the Abstract Syntax Tree. It has attributes value, left, operator, and right. value stores the literal value at leaf nodes, while left and right represent the left and right children of a node. The __repr__ method provides a string representation of the AST node.

### Parser class 
```python
def main():
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message):
        raise Exception(message)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type}, but found {self.current_token.type}")

    def factor(self):
        token = self.current_token
        if token.type == 'INTEGER':
            self.eat('INTEGER')
            return AST(value=token.value)
        else:
            self.error(f"Invalid token: {token.type}")

    def term(self):
        node = self.factor()

        while self.current_token.type in ['MUL', 'DIV']:
            token = self.current_token
            if token.type == 'MUL':
                self.eat('MUL')
            elif token.type == 'DIV':
                self.eat('DIV')

            right_node = self.factor()
            node = AST(left=node, operator=token.value, right=right_node)

        return node

    def expression(self):
        node = self.term()

        while self.current_token.type in ['PLUS', 'MINUS']:
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')

            right_node = self.term()
            node = AST(left=node, operator=token.value, right=right_node)

        return node
```
class Parser: This class implements the parser. It takes a lexer object as input and handles the parsing logic.

__init__(self, lexer): Initializes the parser with a lexer instance and sets the current_token attribute to the first token from the lexer.
error(self, message): Raises an exception with the provided error message.
eat(self, token_type): Compares the type of the current token with the expected token_type. If they match, the parser advances to the next token by calling get_next_token() on the lexer. Otherwise, an error is raised.
factor(self): Parses a factor, which can be either an integer token or an error is raised if the token is invalid.
term(self): Parses a term, which consists of one or more factors multiplied or divided together.
node = self.factor(): Parses the first factor.
while self.current_token.type in ['MUL', 'DIV']:: Loops while the current token is a multiplication or division operator.
token = self.current_token: Stores the current token.
if token.type == 'MUL': or elif token.type == 'DIV':: Checks the type of the operator and advances to the next token accordingly.
right_node = self.factor(): Parses the next factor.
node = AST(left=node, operator=token.value, right=right_node): Constructs an AST node with the current factor as the left child, the operator, and the next factor as the right child. This ensures proper precedence and associativity of the operators.

return node: Returns the resulting AST node.
expression(self): Parses an expression, which consists of one or more terms added or subtracted together. The logic is similar to term(), but with addition and subtraction operators.

### Main class
```python
def main():
    text = "3 + 4 * 2 - 1"
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.expression()

    print(ast)

if __name__ == '__main__':
    main()
```


# Results:
```
/Users/den4k_red/Desktop/UTM/LFAF/Lab3/source/venv/bin/python /Users/den4k_red/Desktop/UTM/LFAF/Lab3/source/main.py 

AST(left=AST(left=AST(value=3), operator=+, right=AST(left=AST(value=4), operator=*, right=AST(value=2))), operator=-, right=AST(value=1))

Process finished with exit code 0
```

# Conclusions
In conclusion, the provided code implements a lexer and parser for processing and parsing arithmetic expressions. The lexer is responsible for tokenizing the input text into meaningful tokens, while the parser analyzes the token stream to construct an Abstract Syntax Tree (AST) that represents the syntactic structure of the expression.

The lexer class Lexer scans the input text character by character, skipping whitespace and recognizing different types of tokens such as integers and operators. It provides a get_next_token() method to retrieve the next token in the input.

The parser class Parser utilizes the lexer to obtain tokens and recursively applies parsing rules to construct the AST. The parser handles operator precedence and associativity by defining separate parsing methods for factors, terms, and expressions. These methods build AST nodes and connect them based on the operators encountered.

The AST class AST represents individual nodes in the Abstract Syntax Tree. It contains attributes such as value, left, operator, and right, allowing for the representation of both leaf nodes (such as integer literals) and internal nodes (such as operators and their operands).

By combining the lexer and parser, the code can parse input text and generate an AST that captures the structure of arithmetic expressions. The resulting AST provides a hierarchical representation of the expression, enabling further analysis or evaluation.

Overall, the implementation showcases the process of lexical analysis and parsing, demonstrating how to break down textual input into meaningful tokens and build a structured representation of the syntax using an AST. This foundation can serve as a starting point for more advanced language processing tasks, such as interpretation or code generation.



