import math

from nova.interpreter.runtime_values import (
    NumberValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_abs(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'abs' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'abs' expects a number.",
            node.line,
            node.column,
        )

    return NumberValue(abs(value.value))


def builtin_min(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'min' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    left = arguments[0]
    right = arguments[1]

    if not isinstance(left, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'min' expects numbers.",
            node.line,
            node.column,
        )

    if not isinstance(right, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'min' expects numbers.",
            node.line,
            node.column,
        )

    return NumberValue(
        min(
            left.value,
            right.value,
        )
    )


def builtin_max(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'max' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    left = arguments[0]
    right = arguments[1]

    if not isinstance(left, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'max' expects numbers.",
            node.line,
            node.column,
        )

    if not isinstance(right, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'max' expects numbers.",
            node.line,
            node.column,
        )

    return NumberValue(
        max(
            left.value,
            right.value,
        )
    )


def builtin_pow(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'pow' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    base = arguments[0]
    exponent = arguments[1]

    if not isinstance(base, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'pow' expects numbers.",
            node.line,
            node.column,
        )

    if not isinstance(exponent, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'pow' expects numbers.",
            node.line,
            node.column,
        )

    return NumberValue(
        pow(
            base.value,
            exponent.value,
        )
    )


def builtin_sqrt(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'sqrt' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'sqrt' expects a number.",
            node.line,
            node.column,
        )

    try:
        return NumberValue(
            math.sqrt(value.value)
        )

    except ValueError:
        raise FunctionArgumentTypeError(
            "Square root of a negative number is undefined.",
            node.line,
            node.column,
        )


def builtin_round(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'round' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'round' expects a number.",
            node.line,
            node.column,
        )

    return NumberValue(
        round(value.value)
    )


def builtin_floor(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'floor' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'floor' expects a number.",
            node.line,
            node.column,
        )

    return NumberValue(
        math.floor(value.value)
    )


def builtin_ceil(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'ceil' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'ceil' expects a number.",
            node.line,
            node.column,
        )

    return NumberValue(
        math.ceil(value.value)
    )