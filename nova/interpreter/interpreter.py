from nova.interpreter.environment import Environment

from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
)

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


class Interpreter:
    def __init__(self):
        self.environment = Environment()

    def interpret(self, program):
        return self.visit(program)

    def visit(self, node):

        if isinstance(node, Program):
            return self.visit_program(node)

        if isinstance(node, VariableDeclaration):
            return self.visit_variable_declaration(node)

        if isinstance(node, Assignment):
            return self.visit_assignment(node)

        if isinstance(node, PrintStatement):
            return self.visit_print_statement(node)

        if isinstance(node, NumberLiteral):
            return self.visit_number_literal(node)

        if isinstance(node, StringLiteral):
            return self.visit_string_literal(node)

        if isinstance(node, Identifier):
            return self.visit_identifier(node)

        if isinstance(node, BinaryExpression):
            return self.visit_binary_expression(node)

        raise Exception(f"Unknown node type: {type(node).__name__}")

    def visit_program(self, node):
        result = None

        for statement in node.statements:
            result = self.visit(statement)

        return result

    def visit_variable_declaration(self, node):
        value = None

        if node.value is not None:
            value = self.visit(node.value)

        self.environment.declare_variable(node.name, node.var_type, value)

        return value

    def visit_assignment(self, node):
        value = self.visit(node.value)

        self.environment.assign_variable(node.name, value)

        return value

    def visit_print_statement(self, node):
        value = self.visit(node.expression)

        print(value.value)

        return value

    def visit_number_literal(self, node):
        return NumberValue(node.value)

    def visit_string_literal(self, node):
        return StringValue(node.value)

    def visit_identifier(self, node):
        return self.environment.get_variable(node.name)

    def visit_binary_expression(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if not isinstance(left, NumberValue):
            raise Exception("Left operand must be numeric.")

        if not isinstance(right, NumberValue):
            raise Exception("Right operand must be numeric.")

        if node.operator == "+":
            return NumberValue(left.value + right.value)

        if node.operator == "-":
            return NumberValue(left.value - right.value)

        if node.operator == "*":
            return NumberValue(left.value * right.value)

        if node.operator == "/":
            return NumberValue(left.value / right.value)

        raise Exception(f"Unknown operator '{node.operator}'")
