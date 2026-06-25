from nova.ast.base import Expression


class Identifier(Expression):
    def __init__(
        self,
        name,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name

    def __repr__(self):
        return f"Identifier({self.name!r})"


class ArrayAccess(Expression):
    def __init__(
        self,
        array,
        index,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.array = array
        self.index = index

    def __repr__(self):
        return f"ArrayAccess(" f"array={self.array}, " f"index={self.index}" f")"


class PropertyAccess(Expression):
    def __init__(
        self,
        target,
        property_name,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.target = target
        self.property_name = property_name

    def __repr__(self):
        return (
            f"PropertyAccess("
            f"target={self.target}, "
            f"property_name={self.property_name!r}"
            f")"
        )


class BinaryExpression(Expression):
    def __init__(
        self,
        left,
        operator,
        right,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

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
    def __init__(
        self,
        operator,
        operand,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return (
            f"UnaryExpression("
            f"operator={self.operator!r}, "
            f"operand={self.operand}"
            f")"
        )


class TernaryExpression(Expression):
    def __init__(
        self,
        condition,
        true_expression,
        false_expression,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.condition = condition
        self.true_expression = true_expression
        self.false_expression = false_expression

    def __repr__(self):
        return (
            f"TernaryExpression("
            f"condition={self.condition}, "
            f"true_expression={self.true_expression}, "
            f"false_expression={self.false_expression}"
            f")"
        )

class FunctionCall(Expression):
    def __init__(
        self,
        callee,
        arguments,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.callee = callee
        self.arguments = arguments

    def __repr__(self):
        return (
            f"FunctionCall("
            f"callee={self.callee}, "
            f"arguments={self.arguments}"
            f")"
        )