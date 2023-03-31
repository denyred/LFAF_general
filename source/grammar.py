import random

class Grammar:
    def __init__(self):
        self.VN = {'S', 'A', 'C', 'D'}
        self.VT = {'a', 'b'}
        self.P = {
            'S': ['aA'],
            'A': ['bS', 'dD'],
            'D': ['bC', 'aD'],
            'C': ['a', 'bA']
        }

    def classify(self):
        # Check if the grammar is type-0
        if not all(len(production) <= len(symbol_string) for symbol_string in self.P.values() for production in
                   symbol_string):
            return "Type-0 (Unrestricted)"

        # Check if the grammar is type-1
        if not all(len(production) < len(symbol_string) for symbol_string in self.P.values() for production in
                   symbol_string if len(production) > 0):
            return "Type-1 (Context-Sensitive)"

        # Check if the grammar is type-2
        if all(len(production) == 1 and production.isupper() for symbol_string in self.P.values() for production in
               symbol_string):
            return "Type-2 (Context-Free)"

        # Check if the grammar is type-3
        if all((len(production) == 2 and production[0] in self.VN and production[1] in self.VT) or production == 'e' for
               symbol_string in self.P.values() for production in symbol_string):
            return "Type-3 (Regular)"

        # If none of the above conditions hold, then the grammar is not a valid Chomsky type
        return "Not a valid Chomsky type"

    def generate_string(self, start_symbol, max_length):
        if max_length == 0:
            return ''
        production = random.choice(self.P[start_symbol])
        string = ''
        for symbol in production:
            if symbol in self.VN:
                string += self.generate_string(symbol, max_length - 1)
            else:
                string += symbol
        return string

    def generate_strings(self, count, max_length):
        strings = []
        for i in range(count):
            strings.append(self.generate_string('S', max_length))
        return strings
