from grammar import Grammar
from finite_automaton import FiniteAutomaton
from Lexer import Lexer, Token
import unittest
from UnitTester import UnitTester
from ChomskyConv import CNFConverter


def main():

    VN = {'S', 'A', 'B', 'C'}
    VI = {'a', 'd'}
    P = [
        ('S', ('d', 'B')),
        ('S', ('A',)),
        ('A', ('d',)),
        ('A', ('d', 'S')),
        ('A', ('a', 'B', 'd', 'A', 'B')),
        ('B', ('a',)),
        ('B', ('d', 'A')),
        ('B', ('A',)),
        ('B', ()),
        ('C', ('A', 'a')),
    ]

    S = 'S'
    grammar = (VN, VI, P, S)

    # Convert the grammar to Chomsky normal form
    cnf_converter = CNFConverter(grammar)
    cnf_grammar = cnf_converter.convert_to_cnf()

    # Print the resulting grammar
    print('Original grammar:')
    print(grammar)
    print('Grammar in Chomsky normal form:')
    print(cnf_grammar)

    #Unit tests 
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(UnitTester))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)


if __name__ == '__main__':
    main()