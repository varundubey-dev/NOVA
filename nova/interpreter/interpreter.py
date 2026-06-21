from nova.interpreter.environment import Environment

from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
    NullValue,
    ArrayValue,
)

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
    ArrayLiteral,
    ArrayAccess,
    ArrayAssignment,
    BinaryExpression,
    UnaryExpression,
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

        if isinstance(node, ConstantDeclaration):
            return self.visit_constant_declaration(node)

        if isinstance(node, Assignment):
            return self.visit_assignment(node)

        if isinstance(node, PrintStatement):
            return self.visit_print_statement(node)

        if isinstance(node, NumberLiteral):
            return self.visit_number_literal(node)

        if isinstance(node, StringLiteral):
            return self.visit_string_literal(node)

        if isinstance(node, BooleanLiteral):
            return self.visit_boolean_literal(node)

        if isinstance(node, NullLiteral):
            return self.visit_null_literal(node)

        if isinstance(node, ArrayLiteral):
            return self.visit_array_literal(node)

        if isinstance(node, ArrayAccess):
            return self.visit_array_access(node)

        if isinstance(node, ArrayAssignment):
            return self.visit_array_assignment(node)

        if isinstance(node, Identifier):
            return self.visit_identifier(node)

        if isinstance(node, UnaryExpression):
            return self.visit_unary_expression(node)

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

        self.environment.declare_variable(
            node.name,
            node.var_type,
            value,
        )

        return value

    def visit_constant_declaration(self, node):
        value = None

        if node.value is not None:
            value = self.visit(node.value)

        self.environment.declare_constant(
            node.name,
            node.const_type,
            value,
        )

        return value

    def visit_assignment(self, node):
        value = self.visit(node.value)

        self.environment.assign_variable(
            node.name,
            value,
        )

        return value

    def visit_print_statement(self, node):
        value = self.visit(node.expression)

        print(self.format_value(value))
        return value

    def visit_number_literal(self, node):
        return NumberValue(node.value)

    def visit_string_literal(self, node):
        return StringValue(node.value)

    def visit_boolean_literal(self, node):
        return BooleanValue(node.value)

    def visit_null_literal(self, node):
        return NullValue()

    def visit_identifier(self, node):
        return self.environment.get_variable(node.name)

    def visit_unary_expression(self, node):
        operand = self.visit(node.operand)

        if node.operator == "!":
            if not isinstance(
                operand,
                BooleanValue,
            ):
                raise Exception("Operand must be boolean.")

            return BooleanValue(not operand.value)

        raise Exception(f"Unknown operator '{node.operator}'")

    def visit_binary_expression(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        # Null protection
        if isinstance(left, NullValue) or isinstance(right, NullValue):
            if node.operator not in (
                "==",
                "!=",
            ):
                raise Exception("Cannot perform operations on null.")

        # Arithmetic
        if node.operator in (
            "+",
            "-",
            "*",
            "/",
            "%",
        ):
            if not isinstance(
                left,
                NumberValue,
            ):
                raise Exception("Left operand must be numeric.")

            if not isinstance(
                right,
                NumberValue,
            ):
                raise Exception("Right operand must be numeric.")

            if node.operator == "+":
                return NumberValue(left.value + right.value)

            if node.operator == "-":
                return NumberValue(left.value - right.value)

            if node.operator == "*":
                return NumberValue(left.value * right.value)

            if node.operator == "/":
                return NumberValue(left.value / right.value)

            if node.operator == "%":
                return NumberValue(left.value % right.value)

        # Comparison
        if node.operator in (
            "<",
            ">",
            "<=",
            ">=",
        ):
            if not isinstance(
                left,
                NumberValue,
            ):
                raise Exception("Left operand must be numeric.")

            if not isinstance(
                right,
                NumberValue,
            ):
                raise Exception("Right operand must be numeric.")

            if node.operator == "<":
                return BooleanValue(left.value < right.value)

            if node.operator == ">":
                return BooleanValue(left.value > right.value)

            if node.operator == "<=":
                return BooleanValue(left.value <= right.value)

            if node.operator == ">=":
                return BooleanValue(left.value >= right.value)

        # Special case: null equality
        if isinstance(left, NullValue) and isinstance(right, NullValue):
            if node.operator == "==":
                return BooleanValue(True)

            if node.operator == "!=":
                return BooleanValue(False)

        # Equality
        assert left is not None
        assert right is not None

        if node.operator == "==":
            return BooleanValue(type(left) is type(right) and left.value == right.value)

        if node.operator == "!=":
            return BooleanValue(
                not (type(left) is type(right) and left.value == right.value)
            )

        # Logical
        if node.operator in (
            "&&",
            "||",
        ):
            if not isinstance(
                left,
                BooleanValue,
            ):
                raise Exception("Left operand must be boolean.")

            if not isinstance(
                right,
                BooleanValue,
            ):
                raise Exception("Right operand must be boolean.")

            if node.operator == "&&":
                return BooleanValue(left.value and right.value)

            if node.operator == "||":
                return BooleanValue(left.value or right.value)

        raise Exception(f"Unknown operator '{node.operator}'")

    def visit_array_literal(self, node):
        elements = []

        for element in node.elements:
            elements.append(self.visit(element))

        return ArrayValue(elements)

    def visit_array_access(self, node):
        array = self.visit(node.array)

        if not isinstance(array, ArrayValue):
            raise Exception("Cannot index non-array value.")

        index = self.visit(node.index)

        if not isinstance(index, NumberValue):
            raise Exception("Array index must be numeric.")

        if not isinstance(index.value, int):
            raise Exception("Array index must be an integer.")

        try:
            return array.value[index.value]

        except IndexError:
            raise Exception("Array index out of bounds.")

    def visit_array_assignment(self, node):
        target = node.target

        if not isinstance(target, ArrayAccess):
            raise Exception("Invalid array assignment.")

        root = self.get_array_root(target)

        if not isinstance(root, Identifier):
            raise Exception("Invalid assignment target.")

        variable_info = self.environment.get_variable_info(root.name)

        if variable_info["constant"]:
            raise Exception("Cannot modify immutable collection.")

        array = self.visit(target.array)

        if not isinstance(array, ArrayValue):
            raise Exception("Cannot index non-array value.")

        index = self.visit(target.index)

        if not isinstance(index, NumberValue):
            raise Exception("Array index must be numeric.")

        if not isinstance(index.value, int):
            raise Exception("Array index must be an integer.")

        value = self.visit(node.value)

        declared_type = variable_info["type"]

        depth = self.get_array_depth(target)

        expected_type = self.get_element_type(
            declared_type,
            depth,
        )

        # Multi-type arrays: [N,S]
        if hasattr(expected_type, "element_types"):
            valid = False

            for allowed_type in expected_type.element_types:
                try:
                    self.environment.validate_type(
                        allowed_type,
                        value,
                    )

                    valid = True
                    break

                except Exception:
                    pass

            if not valid:
                raise Exception("Datatype mismatch.")

        else:
            self.environment.validate_type(
                expected_type,
                value,
            )

        try:
            array.value[index.value] = value

        except IndexError:
            raise Exception("Array index out of bounds.")

        return value

    def get_array_root(self, target):
        current = target

        while isinstance(current, ArrayAccess):
            current = current.array

        return current

    def get_element_type(self, array_type, depth):
        current = array_type

        for _ in range(depth):
            if not hasattr(current, "element_types"):
                return current

            # Multi-type array element
            if len(current.element_types) > 1:
                return current

            current = current.element_types[0]

        return current

    def get_array_depth(self, target):
        depth = 0

        current = target

        while isinstance(current, ArrayAccess):
            depth += 1
            current = current.array

        return depth

    def format_value(self, value):
        if isinstance(value, NumberValue):
            return str(value.value)

        if isinstance(value, StringValue):
            return value.value

        if isinstance(value, BooleanValue):
            return "true" if value.value else "false"

        if isinstance(value, NullValue):
            return "null"

        if isinstance(value, ArrayValue):
            elements = [
                self.format_value(element)
                for element in value.value
            ]

            return "[" + ", ".join(elements) + "]"

        return str(value)
