from nova.lexer.token_types import TokenType

from nova.parser.ast_nodes import (
    Program,
    VariableDeclaration,
    ConstantDeclaration,
    Assignment,
    PrintStatement,
    Identifier,
    NumberLiteral,
    StringLiteral,
    BooleanLiteral,
    NullLiteral,
    ArrayType,
    ArrayLiteral,
    ArrayAccess,
    ArrayAssignment,
    BinaryExpression,
    UnaryExpression,
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
                f"Expected {expected_type.name}, "
                f"got {self.current_token.type.name} "
                f"at line {self.current_token.line}, "
                f"column {self.current_token.column}"
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
            raise Exception("Unexpected EOF while parsing statement")

        if self.current_token.type == TokenType.PRINT:
            return self.parse_print_statement()

        if self.current_token.type == TokenType.IDENTIFIER:
            next_token = self.peek()

            if next_token is None:
                raise Exception("Unexpected EOF while parsing statement")

            if next_token.type == TokenType.COLON:
                return self.parse_variable_declaration()

            if next_token.type == TokenType.DOUBLE_COLON:
                return self.parse_constant_declaration()

            if next_token.type == TokenType.LBRACKET:
                if self.is_array_assignment():
                    return self.parse_array_assignment()

            if next_token.type == TokenType.EQUALS:
                return self.parse_assignment()

        raise Exception(
            f"Unexpected token {self.current_token.type.name} "
            f"at line {self.current_token.line}, "
            f"column {self.current_token.column}"
        )

    def parse_variable_declaration(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.COLON)

        var_type = self.parse_type()

        value = None

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.EQUALS
        ):
            self.advance()

            value = self.parse_expression()

        return VariableDeclaration(
            name=name_token.value,
            var_type=var_type,
            value=value,
        )

    def parse_constant_declaration(self):
        name_token = self.consume(TokenType.IDENTIFIER)

        self.consume(TokenType.DOUBLE_COLON)

        const_type = self.parse_type()

        value = None

        if (
            self.current_token is not None
            and self.current_token.type == TokenType.EQUALS
        ):
            self.advance()

            value = self.parse_expression()

        return ConstantDeclaration(
            name=name_token.value,
            const_type=const_type,
            value=value,
        )

    def parse_type(self):
        if self.current_token is None:
            raise Exception("Unexpected EOF while parsing type")

        if self.current_token.type == TokenType.TYPE:
            token = self.current_token

            self.advance()

            return token.value

        if self.current_token.type == TokenType.LBRACKET:
            return self.parse_array_type()

        raise Exception(
            f"Expected type at line {self.current_token.line}, "
            f"column {self.current_token.column}"
        )

    def parse_array_type(self):
        self.consume(TokenType.LBRACKET)

        element_types = []

        while True:
            element_types.append(self.parse_type())

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()
                continue

            break

        self.consume(TokenType.RBRACKET)

        return ArrayType(element_types)

    def parse_array_literal(self):
        self.consume(TokenType.LBRACKET)

        elements = []

        self.skip_newlines()

        # Empty array: []
        if (
            self.current_token is not None
            and self.current_token.type == TokenType.RBRACKET
        ):
            self.advance()

            return ArrayLiteral(elements)

        while True:
            self.skip_newlines()

            elements.append(self.parse_expression())

            self.skip_newlines()

            if (
                self.current_token is not None
                and self.current_token.type == TokenType.COMMA
            ):
                self.advance()

                self.skip_newlines()

                continue

            break

        self.consume(TokenType.RBRACKET)

        return ArrayLiteral(elements)

    def skip_newlines(self):
        while (
            self.current_token is not None
            and self.current_token.type == TokenType.NEWLINE
        ):
            self.advance()

    def parse_array_access(self, expression):
        while (
            self.current_token is not None
            and self.current_token.type == TokenType.LBRACKET
        ):
            self.advance()

            index = self.parse_expression()

            self.consume(TokenType.RBRACKET)

            expression = ArrayAccess(
                array=expression,
                index=index,
            )

        return expression

    def is_array_assignment(self):
        pos = self.position + 1

        bracket_depth = 0
        seen_brackets = False

        while pos < len(self.tokens):
            token = self.tokens[pos]

            if token.type == TokenType.LBRACKET:
                bracket_depth += 1
                seen_brackets = True

            elif token.type == TokenType.RBRACKET:
                bracket_depth -= 1

            elif (
                seen_brackets and bracket_depth == 0 and token.type == TokenType.EQUALS
            ):
                return True

            elif (
                seen_brackets
                and bracket_depth == 0
                and token.type
                not in (
                    TokenType.LBRACKET,
                    TokenType.EQUALS,
                )
            ):
                return False

            pos += 1

        return False

    def parse_array_assignment(self):
        target = Identifier(self.consume(TokenType.IDENTIFIER).value)

        target = self.parse_array_access(target)

        self.consume(TokenType.EQUALS)

        value = self.parse_expression()

        return ArrayAssignment(
            target=target,
            value=value,
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
        return self.parse_or()

    def parse_or(self):
        left = self.parse_and()

        while (
            self.current_token is not None and self.current_token.type == TokenType.OR
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_and()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_and(self):
        left = self.parse_equality()

        while (
            self.current_token is not None and self.current_token.type == TokenType.AND
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_equality()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_equality(self):
        left = self.parse_comparison()

        while self.current_token is not None and self.current_token.type in (
            TokenType.EQUAL_EQUAL,
            TokenType.NOT_EQUAL,
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_comparison()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_comparison(self):
        left = self.parse_additive()

        while self.current_token is not None and self.current_token.type in (
            TokenType.LESS,
            TokenType.GREATER,
            TokenType.LESS_EQUAL,
            TokenType.GREATER_EQUAL,
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_additive()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_additive(self):
        left = self.parse_multiplicative()

        while self.current_token is not None and self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_multiplicative()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_multiplicative(self):
        left = self.parse_unary()

        while self.current_token is not None and self.current_token.type in (
            TokenType.STAR,
            TokenType.SLASH,
            TokenType.MODULO,
        ):
            operator = self.current_token.value

            self.advance()

            right = self.parse_unary()

            left = BinaryExpression(left, operator, right)

        return left

    def parse_unary(self):
        if self.current_token is not None and self.current_token.type == TokenType.NOT:
            operator = self.current_token.value

            self.advance()

            operand = self.parse_unary()

            return UnaryExpression(operator, operand)

        return self.parse_primary()

    def parse_primary(self):
        if self.current_token is None:
            raise Exception("Unexpected EOF while parsing expression")

        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(token.value)

        if token.type == TokenType.STRING:
            self.advance()
            return StringLiteral(token.value)

        if token.type == TokenType.BOOLEAN:
            self.advance()
            return BooleanLiteral(token.value)

        if token.type == TokenType.NULL:
            self.advance()
            return NullLiteral()

        if token.type == TokenType.LBRACKET:
            return self.parse_array_literal()

        if token.type == TokenType.IDENTIFIER:
            self.advance()
            expression = Identifier(token.value)
            return self.parse_array_access(expression)

        if token.type == TokenType.LPAREN:
            self.advance()

            expression = self.parse_expression()

            self.consume(TokenType.RPAREN)

            return expression

        raise Exception(
            f"Unexpected token {token.type.name} "
            f"at line {token.line}, "
            f"column {token.column}"
        )
