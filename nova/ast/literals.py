from nova.ast.base import Expression
from nova.ast.base import Node


class NumberLiteral(Expression):
    def __init__(
        self,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"NumberLiteral({self.value})"


class StringLiteral(Expression):
    def __init__(
        self,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"StringLiteral({self.value!r})"


class BooleanLiteral(Expression):
    def __init__(
        self,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.value = value

    def __repr__(self):
        return f"BooleanLiteral({self.value})"


class NullLiteral(Expression):
    def __init__(
        self,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

    def __repr__(self):
        return "NullLiteral()"


class ArrayLiteral(Expression):
    def __init__(
        self,
        elements,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.elements = elements

    def __repr__(self):
        return f"ArrayLiteral({self.elements})"


class MapEntry(Node):
    def __init__(
        self,
        key,
        value,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.key = key
        self.value = value

    def __repr__(self):
        return f"MapEntry(" f"key={self.key!r}, " f"value={self.value}" f")"


class MapLiteral(Expression):
    def __init__(
        self,
        entries,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.entries = entries

    def __repr__(self):
        return f"MapLiteral({self.entries})"
