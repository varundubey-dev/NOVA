import random

from nova.interpreter.runtime_values import (
    NumberValue,
    ArrayValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_random(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 0:
        raise FunctionArgumentCountError(
            f"Function 'random' expects 0 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    return NumberValue(
        random.random()
    )


def builtin_randint(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'randint' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    minimum = arguments[0]
    maximum = arguments[1]

    if not isinstance(minimum, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'randint' expects numbers.",
            node.line,
            node.column,
        )

    if not isinstance(maximum, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'randint' expects numbers.",
            node.line,
            node.column,
        )

    return NumberValue(
        random.randint(
            int(minimum.value),
            int(maximum.value),
        )
    )


def builtin_choice(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'choice' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'choice' expects an array.",
            node.line,
            node.column,
        )

    if len(values.value) == 0:
        raise FunctionArgumentTypeError(
            "Cannot choose from an empty array.",
            node.line,
            node.column,
        )

    return random.choice(values.value)


def builtin_shuffle(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'shuffle' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = arguments[0]

    if not isinstance(values, ArrayValue):
        raise FunctionArgumentTypeError(
            "Function 'shuffle' expects an array.",
            node.line,
            node.column,
        )

    random.shuffle(values.value)

    return values


def builtin_seed(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'seed' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'seed' expects a number.",
            node.line,
            node.column,
        )

    random.seed(value.value)

    return None