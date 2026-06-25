from nova.interpreter.expressions import ExpressionInterpreter
from nova.interpreter.type_resolver import TypeResolver

from nova.interpreter.runtime_values import (
    NumberValue,
    ArrayValue,
    MapValue,
)

from nova.ast import Identifier, ArrayAccess, PropertyAccess, ArrayType

from nova.errors import (
    InvalidArrayAccessError,
    InvalidArrayIndexError,
    InvalidArrayAssignmentError,
    InvalidOperandError,
    DatatypeMismatchError,
    ConstantReassignmentError,
)


class CollectionInterpreter(TypeResolver, ExpressionInterpreter):

    # Schemas

    def visit_schema_declaration(self, node):
        self.environment.declare_schema(
            node.name,
            node.schema,
            node.line,
            node.column,
        )

        return None

    # Map Literals

    def visit_map_literal(self, node):
        properties = {}

        for entry in node.entries:
            properties[entry.key] = self.visit(entry.value)

        return MapValue(properties)

    # Array Literals

    def visit_array_literal(self, node):
        elements = []

        for element in node.elements:
            elements.append(self.visit(element))

        return ArrayValue(elements)

    # Property Access

    def visit_property_access(self, node):
        target = self.visit(node.target)

        if not isinstance(target, MapValue):
            raise InvalidOperandError(
                "Cannot access property on non-map value.",
                node.line,
                node.column,
            )

        if node.property_name not in target.value:
            raise InvalidOperandError(
                f"Unknown property '{node.property_name}'.",
                node.line,
                node.column,
            )

        return target.value[node.property_name]

    # Array Access

    def visit_array_access(self, node):
        array = self.visit(node.array)

        if not isinstance(array, ArrayValue):
            raise InvalidArrayAccessError(
                "Cannot index non-array value.",
                node.line,
                node.column,
            )

        index = self.visit(node.index)

        if not isinstance(index, NumberValue):
            raise InvalidArrayIndexError(
                "Array index must be numeric.",
                node.line,
                node.column,
            )

        if not isinstance(index.value, int):
            raise InvalidArrayIndexError(
                "Array index must be an integer.",
                node.line,
                node.column,
            )

        try:
            return array.value[index.value]

        except IndexError:
            raise InvalidArrayIndexError(
                "Array index out of bounds.",
                node.line,
                node.column,
            )

    # Property Assignment

    def visit_property_assignment(self, node):
        if self.is_immutable_collection(node.target):
            raise ConstantReassignmentError(
                "Cannot modify immutable collection.",
                node.line,
                node.column,
            )

        target = node.target

        parent = self.visit(target.target)

        if not isinstance(parent, MapValue):
            raise InvalidOperandError(
                "Cannot access property on non-map value.",
                node.line,
                node.column,
            )

        property_name = target.property_name

        if property_name not in parent.value:
            raise InvalidOperandError(
                f"Unknown property '{property_name}'.",
                node.line,
                node.column,
            )

        value = self.visit(node.value)

        field = self.get_property_schema_field(target)

        self.environment.validate_type(
            field.field_type,
            value,
            node.line,
            node.column,
        )

        parent.value[property_name] = value

        return value

    # Array Assignment

    def visit_array_assignment(self, node):
        target = node.target

        if not isinstance(target, ArrayAccess):
            raise InvalidArrayAssignmentError(
                "Invalid array assignment.",
                node.line,
                node.column,
            )

        if self.is_immutable_collection(target):
            raise ConstantReassignmentError(
                "Cannot modify immutable collection.",
                node.line,
                node.column,
            )

        array = self.visit(target.array)

        if not isinstance(array, ArrayValue):
            raise InvalidArrayAccessError(
                "Cannot index non-array value.",
                node.line,
                node.column,
            )

        index = self.visit(target.index)

        if not isinstance(index, NumberValue):
            raise InvalidArrayIndexError(
                "Array index must be numeric.",
                node.line,
                node.column,
            )

        if not isinstance(index.value, int):
            raise InvalidArrayIndexError(
                "Array index must be an integer.",
                node.line,
                node.column,
            )

        value = self.visit(node.value)

        expected_type = self.get_array_assignment_type(target)

        # Multi-type arrays
        if isinstance(
            expected_type,
            ArrayType,
        ):
            valid = False

            for allowed_type in expected_type.element_types:
                try:
                    self.environment.validate_type(
                        allowed_type,
                        value,
                        node.line,
                        node.column,
                    )

                    valid = True
                    break

                except DatatypeMismatchError:
                    pass

            if not valid:
                raise DatatypeMismatchError(
                    "Datatype mismatch.",
                    node.line,
                    node.column,
                )

        else:
            self.environment.validate_type(
                expected_type,
                value,
                node.line,
                node.column,
            )

        try:
            array.value[index.value] = value

        except IndexError:
            raise InvalidArrayIndexError(
                "Array index out of bounds.",
                node.line,
                node.column,
            )

        return value

    # Helpers

    def get_array_root(self, target):
        current = target

        while isinstance(current, ArrayAccess):
            current = current.array

        return current

    def get_collection_root(
        self,
        target,
    ):
        current = target

        while True:

            if isinstance(
                current,
                PropertyAccess,
            ):
                current = current.target
                continue

            if isinstance(
                current,
                ArrayAccess,
            ):
                current = current.array
                continue

            break

        return current

    def is_immutable_collection(
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

        if not isinstance(current, Identifier):
            return False

        variable_info = self.environment.get_variable_info(
            current.name,
            target.line,
            target.column,
        )

        return variable_info["constant"]