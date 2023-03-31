from grammar import Grammar
from finite_automaton import FiniteAutomaton
from Lexer import Lexer, Token

def main():
        # Define input text
        text = "3 + 4 * 2 - 1"


        # Create lexer object
        lexer = Lexer(text)

        token = lexer.get_next_token()

        while token.type != "EOF":
            print(token)
            token = lexer.get_next_token()

        print(token)

if __name__ == '__main__':
    main()
