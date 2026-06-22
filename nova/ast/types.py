from nova.ast.base import Node


class ArrayType(Node):
    def __init__(
        self,
        element_types,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.element_types = element_types

    def __repr__(self):
        return f"ArrayType({self.element_types})"


class SchemaField(Node):
    def __init__(
        self,
        name,
        field_type,
        optional=False,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.name = name
        self.field_type = field_type
        self.optional = optional

    def __repr__(self):
        return (
            f"SchemaField("
            f"name={self.name!r}, "
            f"field_type={self.field_type!r}, "
            f"optional={self.optional}"
            f")"
        )


class SchemaType(Node):
    def __init__(
        self,
        fields,
        line=None,
        column=None,
    ):
        super().__init__(line, column)

        self.fields = fields

    def __repr__(self):
        return f"SchemaType({self.fields})"
