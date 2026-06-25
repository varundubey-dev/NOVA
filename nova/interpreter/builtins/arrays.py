from nova.interpreter.runtime_values import (
    ArrayValue,
    StringValue,
    NumberValue,
    BooleanValue,
    NullValue
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_length(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'length' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if isinstance(value, ArrayValue):
        return NumberValue(len(value.value))

    if isinstance(value, StringValue):
        return NumberValue(len(value.value))

    raise FunctionArgumentTypeError(
        "Function 'length' expects an array or string.",
        node.line,
        node.column,
    )


def builtin_push(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'push' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    array = arguments[0]
    value = arguments[1]

    if not isinstance(array, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'push' expects an array.",
            node.line,
            node.column,
        )

    expected_type = interpreter.get_array_element_type(
        argument_nodes[0]
    )

    interpreter.environment.validate_type(
        expected_type,
        value,
        node.line,
        node.column,
    )

    array.value.append(value)

    return NullValue()


def builtin_pop(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'pop' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    array = arguments[0]

    if not isinstance(array, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'pop' expects an array.",
            node.line,
            node.column,
        )

    if len(array.value) == 0:
        raise FunctionArgumentTypeError(
            "Cannot pop from an empty array.",
            node.line,
            node.column,
        )

    return array.value.pop()


def builtin_insert(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 3:
        raise FunctionArgumentCountError(
            f"Function 'insert' expects 3 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    array = arguments[0]
    index = arguments[1]
    value = arguments[2]

    if not isinstance(array, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'insert' expects an array.",
            node.line,
            node.column,
        )

    if not isinstance(index, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'insert' expects a numeric index.",
            node.line,
            node.column,
        )

    if not isinstance(index.value, int):
        raise FunctionArgumentTypeError(
            "Array index must be an integer.",
            node.line,
            node.column,
        )

    if index.value < 0 or index.value > len(array.value):
        raise FunctionArgumentTypeError(
            "Array index out of bounds.",
            node.line,
            node.column,
        )

    expected_type = interpreter.get_array_element_type(
        argument_nodes[0]
    )

    interpreter.environment.validate_type(
        expected_type,
        value,
        node.line,
        node.column,
    )

    array.value.insert(
        index.value,
        value,
    )

    return NullValue()

def builtin_remove(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'remove' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    array = arguments[0]
    index = arguments[1]

    if not isinstance(array, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'remove' expects an array.",
            node.line,
            node.column,
        )

    if not isinstance(index, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'remove' expects a numeric index.",
            node.line,
            node.column,
        )

    if not isinstance(index.value, int):
        raise FunctionArgumentTypeError(
            "Array index must be an integer.",
            node.line,
            node.column,
        )

    try:
        array.value.pop(index.value)

    except IndexError:
        raise FunctionArgumentTypeError(
            "Array index out of bounds.",
            node.line,
            node.column,
        )

    return NullValue()

def builtin_contains(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'contains' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    collection = arguments[0]
    value = arguments[1]

    # Array contains
    if isinstance(collection, ArrayValue):
        return BooleanValue(value in collection.value)

    # String contains
    if isinstance(collection, StringValue):
        if not isinstance(value, StringValue):
            raise FunctionArgumentTypeError(
                "Function 'contains' expects a string as the second argument.",
                node.line,
                node.column,
            )

        return BooleanValue(value.value in collection.value)

    raise FunctionArgumentTypeError(
        "Function 'contains' expects an array or string as the first argument.",
        node.line,
        node.column,
    )


def builtin_clear(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'clear' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    array = arguments[0]

    if not isinstance(array, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'clear' expects an array.",
            node.line,
            node.column,
        )

    array.value.clear()

    return NullValue()