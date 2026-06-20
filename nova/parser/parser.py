from nova.lexer.token_types import TokenType

from nova.parser.ast_nodes import (
    Program,
    VariableDeclaration,
    Assignment,
    PrintStatement,
    Identifier,
    NumberLiteral,
    StringLiteral,
    BinaryExpression,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

        self.position = 0

        self.current_token = tokens[0] if tokens else None

    def advance(self):
        self.position += 1

        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def peek(self):
        next_position = self.position + 1

        if next_position >= len(self.tokens):
            return None

        return self.tokens[next_position]

    def consume(self, expected_type):
        if self.current_token is None:
            raise Exception(f"Expected {expected_type.name}, got EOF")

        if self.current_token.type != expected_type:
            raise Exception(
                f"Expected {expected_type.name}, " f"got {self.current_token.type.name}"
            )

        token = self.current_token

        self.advance()

        return token

    def parse(self):
        statements = []

        while (
            self.current_token is not None and self.current_token.type != TokenType.EOF
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue

            statements.append(self.parse_statement())

        return Program(statements)

    def parse_statement(self):
        if self.current_token is None:
            raise Exception("Unexpected EOF")

        if self.current_token.type == TokenType.PRINT:
            return self.parse_print_statement()

        if self.current_token.type == TokenType.IDENTIFIER:
            next_token = self.peek()

            if next_token is None:
                raise Exception("Unexpected EOF")

            if next_token.type == TokenType.COLON:
                return self.parse_variable_declaration()

            if next_token.type == TokenType.EQUALS:
                return self.parse_assignment()

        raise Exception(f"Unexpected token {self.current_token.type.name}")

    def parse_variable_declaration(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.COLON)

        type_token = self.consume(TokenType.TYPE)

        value = None

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.EQUALS
        ):
            self.advance()

            value = self.parse_expression()

        return VariableDeclaration(
            name=name_token.value, var_type=type_token.value, value=value
        )

    def parse_assignment(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.EQUALS)

        value = self.parse_expression()

        return Assignment(name=name_token.value, value=value)

    def parse_print_statement(self):
        self.consume(TokenType.PRINT)

        self.consume(TokenType.LPAREN)

        expression = self.parse_expression()

        self.consume(TokenType.RPAREN)

        return PrintStatement(expression)

    def parse_expression(self):
        left = self.parse_term()

        while self.current_token is not None and self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_term()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.current_token is not None and self.current_token.type in (
            TokenType.STAR,
            TokenType.SLASH,
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_factor()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_factor(self):
        if self.current_token is None:
            raise Exception("Unexpected EOF")

        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(token.value)

        if token.type == TokenType.STRING:
            self.advance()
            return StringLiteral(token.value)

        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return Identifier(token.value)

        if token.type == TokenType.LPAREN:
            self.advance()

            expression = self.parse_expression()

            self.consume(TokenType.RPAREN)

            return expression

        raise Exception(f"Unexpected token {token.type.name}")
