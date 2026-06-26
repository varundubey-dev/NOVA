from nova.interpreter.runtime_values import (
    NumberValue,
    ArrayValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_sort(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'sort' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'sort' expects an array.",
            node.line,
            node.column,
        )

    values.value.sort(
        key=lambda value: value.value
    )

    return values


def builtin_reverse(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'reverse' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'reverse' expects an array.",
            node.line,
            node.column,
        )

    values.value.reverse()

    return values


def builtin_unique(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'unique' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'unique' expects an array.",
            node.line,
            node.column,
        )

    unique = []

    for element in values.value:
        if not any(
            type(existing) is type(element)
            and existing.value == element.value
            for existing in unique
        ):
            unique.append(element)

    return ArrayValue(unique)


def builtin_count(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'count' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]
    target = arguments[1]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'count' expects an array.",
            node.line,
            node.column,
        )

    count = 0

    for element in values.value:
        if (
            type(element) is type(target)
            and element.value == target.value
        ):
            count += 1

    return NumberValue(count)


def builtin_index_of(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'indexOf' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]
    target = arguments[1]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'indexOf' expects an array.",
            node.line,
            node.column,
        )

    for index, element in enumerate(values.value):
        if (
            type(element) is type(target)
            and element.value == target.value
        ):
            return NumberValue(index)

    return NumberValue(-1)