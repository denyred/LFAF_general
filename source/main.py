from grammar import Grammar
from finite_automaton import FiniteAutomaton
from Lexer import Lexer, Token
from Parser import Parser, AST
from UnitTester import UnitTester
from ChomskyConv import CNFConverter


def main():
    text = "3 + 4 * 2 - 1"
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.expression()

    print(ast)

if __name__ == '__main__':
    main()