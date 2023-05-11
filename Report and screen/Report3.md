# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Spataru Dionisie FAF-211





## Theory
    Lexer, also known as lexical analysis, is the process of extracting lexical tokens from a sequence of characters. It plays a crucial role in the early stages of compiling or interpreting programming, markup, or other types of languages. The lexer, sometimes referred to as a tokenizer or scanner, operates by applying the language's predefined rules to identify and categorize tokens. These tokens represent meaningful units of the language's syntax and are typically derived by splitting the input string using delimiters like spaces.

Each token is associated with a lexeme, which is the actual substring of characters that corresponds to the token. While the lexeme captures the value of the token, the token itself primarily provides a name or category for the lexeme. For instance, a token might be labeled as an "identifier" or "integer literal," indicating the type of information it represents in the language.

In addition to the lexeme and category, tokens often include additional metadata. This metadata can include information like the position of the token in the source code, line numbers, and other relevant details that aid in subsequent stages of language processing.

The lexer's primary responsibility is to break down the input string into individual tokens, facilitating the subsequent stages of parsing and interpretation. By isolating the fundamental building blocks of a language's syntax, the lexer enables compilers, interpreters, and other language processing tools to analyze and manipulate the code effectively.

## Objectives:
- Understand what lexical analysis [1] is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
In Python, the Lexer class is responsible for analyzing an input string and recognizing the different types of tokens present within it. It accomplishes this task by defining a collection of regular expression patterns that correspond to various token categories, including operators, identifiers, keywords, numbers, strings, and more. By specifying these patterns, the class establishes the rules for token identification.

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
### Tokenize method
Within a lexer file, the class token serves as a representation of a particular category or type of lexeme that has been recognized by the lexer. These tokens hold essential information like the type of the lexeme and any associated metadata. However, they typically do not retain the exact value of the lexeme itself. The token class is commonly utilized to define and classify different types of tokens that can appear in the input source code or document, including keywords, identifiers, operators, or literals.

During the lexer's operation, it analyzes the input and generates these tokens based on the identified lexemes. Each token is then passed to subsequent stages of the compiler or interpreter for further processing. By encapsulating the necessary details and categorization of lexemes, tokens enable subsequent stages to perform tasks such as syntax analysis, semantic evaluation, and code generation more effectively.

In summary, the token class plays a vital role in the lexer's workflow, allowing the identification and organization of lexemes into meaningful categories. These tokens serve as intermediaries, conveying important information about the lexemes to subsequent stages of language processing, ultimately aiding in the comprehensive analysis and interpretation of the input source code.

### Main
In the Main class, the Lexer class from the lexer module is imported, allowing access to its functionalities. An instance of the Lexer class is created by calling its constructor without any arguments. This instance represents the lexer object responsible for tokenizing input strings.

To tokenize a specific input string, the tokenize method of the lexer instance is invoked. In this case, the input string passed to the method is "3 + 4 * 2 - 1". The tokenize method processes the input string, splitting it into a list of tokens based on predefined rules and patterns. This list of tokens is then returned by the method.

To verify the correctness of the tokenization process, the resulting list of tokens is printed to the console using the print function. The output showcases the successful tokenization of the input string, revealing the individual tokens such as numbers, operators, and parentheses.

Additionally, if the tokenization process completes without encountering any errors, a message of "input valid" is displayed on the console. This message confirms that the input string was successfully tokenized without any issues.

Overall, this code snippet demonstrates the usage of the Lexer class to tokenize an input string, providing a structured representation of the constituent tokens, and indicating the successful tokenization of the input.

```python
 # Define input text
        text = "3 + 4 * 2 - 1"


        # Create lexer object
        lexer = Lexer(text)

        token = lexer.get_next_token()

        while token.type != "EOF":
            print(token)
            token = lexer.get_next_token()

        print(token)

```



## Results
Token(type='INTEGER', value=3)
Token(type='PLUS', value=+)
Token(type='INTEGER', value=4)
Token(type='MUL', value=*)
Token(type='INTEGER', value=2)
Token(type='MINUS', value=-)
Token(type='INTEGER', value=1)
Token(type='EOF', value=None)


## Conclusions
A lexer plays a critical role in the processing of programming languages, as it is responsible for breaking down an input string into tokens that represent meaningful elements of the language. These tokens are essential for understanding and analyzing the code's syntax and semantics, as they are mapped to specific types and interpretations defined by production rules.

The lexer's significance extends beyond the mere tokenization process. It is often utilized in various programming tools and IDEs for tasks such as syntax highlighting, code completion, and program analysis. Syntax highlighting involves visually distinguishing different token types by applying distinct colors or styles, aiding developers in visually understanding the structure of their code. Code completion uses the lexer's knowledge of token types to suggest and auto-complete code snippets or identifiers, improving productivity. Program analysis relies on the lexer to extract information from the code, enabling tasks like identifying code patterns, detecting potential issues, or extracting program metrics.

Implementing a lexer in Python using regular expressions is a common approach due to its flexibility and efficiency. Regular expressions provide a concise and powerful way to define the syntax of a language, allowing for easy matching of token patterns. By iterating over the input string and applying regular expressions, the lexer can efficiently identify and generate corresponding tokens.

The project showcasing this lexer implementation serves as a valuable example of how lexers are fundamental building blocks in language processing. It highlights their crucial role in enabling the development of advanced compilers, interpreters, and analysis tools. With a lexer, one can pave the way for comprehensive code understanding, error detection, optimization, and various other language-specific functionalities.

Overall, the project emphasizes the importance of lexers in programming language processing and showcases their potential for empowering developers with powerful tools for code analysis, understanding, and improvement.