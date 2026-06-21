class Node:
    pass


class Statement(Node):
    pass


class Expression(Node):
    pass


class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"


class VariableDeclaration(Statement):
    def __init__(self, name, var_type, value=None):
        self.name = name
        self.var_type = var_type
        self.value = value

    def __repr__(self):
        return (
            f"VariableDeclaration("
            f"name={self.name!r}, "
            f"var_type={self.var_type!r}, "
            f"value={self.value}"
            f")"
        )


class ConstantDeclaration(Statement):
    def __init__(self, name, const_type, value=None):
        self.name = name
        self.const_type = const_type
        self.value = value

    def __repr__(self):
        return (
            f"ConstantDeclaration("
            f"name={self.name!r}, "
            f"const_type={self.const_type!r}, "
            f"value={self.value}"
            f")"
        )


class Assignment(Statement):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment(" f"name={self.name!r}, " f"value={self.value}" f")"


class PrintStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"PrintStatement({self.expression})"


class Identifier(Expression):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name!r})"


class NumberLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberLiteral({self.value})"


class StringLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"StringLiteral({self.value!r})"


class BooleanLiteral(Expression):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"BooleanLiteral({self.value})"


class NullLiteral(Expression):
    def __init__(self):
        pass

    def __repr__(self):
        return "NullLiteral()"


class BinaryExpression(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return (
            f"BinaryExpression("
            f"left={self.left}, "
            f"operator={self.operator!r}, "
            f"right={self.right}"
            f")"
        )


class UnaryExpression(Expression):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return (
            f"UnaryExpression("
            f"operator={self.operator!r}, "
            f"operand={self.operand}"
            f")"
        )
