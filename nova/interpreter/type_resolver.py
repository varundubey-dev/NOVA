from nova.ast import (
    Identifier,
    ArrayAccess,
    PropertyAccess,
    ArrayType,
)

from nova.errors import (
    DatatypeMismatchError,
)


class TypeResolver:
    def get_collection_root(
        self,
        target,
    ):
        current = target

        while True:

            if isinstance(current, PropertyAccess):
                current = current.target
                continue

            if isinstance(current, ArrayAccess):
                current = current.array
                continue

            break

        return current

    def get_array_depth(
        self,
        target,
    ):
        depth = 0

        current = target

        while isinstance(current, ArrayAccess):
            depth += 1
            current = current.array

        return depth

    def get_element_type(
        self,
        array_type,
        depth,
    ):
        current = array_type

        for _ in range(depth):

            if not isinstance(current, ArrayType):
                return current

            if len(current.element_types) > 1:
                return current

            current = current.element_types[0]

        return current

    def get_property_schema_field(
        self,
        target,
    ):
        root = self.get_collection_root(target)

        if not isinstance(root, Identifier):
            raise DatatypeMismatchError(
                "Invalid property access.",
                target.line,
                target.column,
            )

        variable_info = self.environment.get_variable_info(
            root.name,
            target.line,
            target.column,
        )

        variable_type = variable_info["type"]

        chain = []

        current = target

        while True:

            if isinstance(current, PropertyAccess):
                chain.append(
                    (
                        "property",
                        current.property_name,
                    )
                )
                current = current.target
                continue

            if isinstance(current, ArrayAccess):
                chain.append(
                    (
                        "array",
                        None,
                    )
                )
                current = current.array
                continue

            break

        chain.reverse()

        current_type = variable_type

        for kind, value in chain:

            if kind == "array":

                current_type = self.get_element_type(
                    current_type,
                    1,
                )

                continue

            schema = self.environment.get_schema(
                current_type,
                target.line,
                target.column,
            )

            field_lookup = {field.name: field for field in schema.fields}

            field = field_lookup.get(value)

            if field is None:
                raise DatatypeMismatchError(
                    f"Unknown property '{value}'.",
                    target.line,
                    target.column,
                )

            current_type = field.field_type

            if (kind, value) == chain[-1]:
                return field

        raise DatatypeMismatchError(
            "Invalid property access.",
            target.line,
            target.column,
        )

    def get_array_assignment_type(
        self,
        target,
    ):
        parent = target.array

        if isinstance(parent, PropertyAccess):

            field = self.get_property_schema_field(parent)

            if not isinstance(field.field_type, ArrayType):
                return "U"

            return field.field_type.element_types[0]

        if isinstance(parent, ArrayAccess):

            root = self.get_collection_root(parent)

            if not isinstance(root, Identifier):
                raise DatatypeMismatchError(
                    "Invalid array access.",
                    target.line,
                    target.column,
                )

            variable_info = self.environment.get_variable_info(
                root.name,
                target.line,
                target.column,
            )

            depth = self.get_array_depth(target)

            return self.get_element_type(
                variable_info["type"],
                depth,
            )

        root = self.get_collection_root(target)

        if not isinstance(root, Identifier):
            raise DatatypeMismatchError(
                "Invalid array access.",
                target.line,
                target.column,
            )

        variable_info = self.environment.get_variable_info(
            root.name,
            target.line,
            target.column,
        )

        depth = self.get_array_depth(target)

        return self.get_element_type(
            variable_info["type"],
            depth,
        )

    def get_array_element_type(
        self,
        target,
    ):
        # Variable
        if isinstance(target, Identifier):

            variable_info = self.environment.get_variable_info(
                target.name,
                target.line,
                target.column,
            )

            variable_type = variable_info["type"]

            if not isinstance(variable_type, ArrayType):
                raise DatatypeMismatchError(
                    "Expected an array.",
                    target.line,
                    target.column,
                )

            return variable_type.element_types[0]

        # Property (user.scores)
        if isinstance(target, PropertyAccess):

            field = self.get_property_schema_field(
                target,
            )

            if not isinstance(field.field_type, ArrayType):
                raise DatatypeMismatchError(
                    "Expected an array.",
                    target.line,
                    target.column,
                )

            return field.field_type.element_types[0]

        # Nested array (matrix[0], cube[0][1], user.scores[0])
        if isinstance(target, ArrayAccess):

            root = self.get_collection_root(
                target,
            )

            if not isinstance(root, Identifier):
                raise DatatypeMismatchError(
                    "Invalid array access.",
                    target.line,
                    target.column,
                )

            variable_info = self.environment.get_variable_info(
                root.name,
                target.line,
                target.column,
            )

            depth = self.get_array_depth(
                target,
            )

            current_type = self.get_element_type(
                variable_info["type"],
                depth,
            )

            if not isinstance(current_type, ArrayType):
                raise DatatypeMismatchError(
                    "Expected an array.",
                    target.line,
                    target.column,
                )

            return current_type.element_types[0]

        raise DatatypeMismatchError(
            "Expected an array.",
            target.line,
            target.column,
        )
