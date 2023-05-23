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