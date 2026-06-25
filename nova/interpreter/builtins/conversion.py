from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_to_string(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'toString' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    return StringValue(
        interpreter.format_value(value)
    )


def builtin_to_number(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'toNumber' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'toNumber' expects a string.",
            node.line,
            node.column,
        )

    try:
        text = value.value.strip()

        if any(c in text for c in (".", "e", "E")):
            number = float(text)
        else:
            number = int(text)

        return NumberValue(number)

    except ValueError:
        raise FunctionArgumentTypeError(
            "Invalid numeric conversion.",
            node.line,
            node.column,
        )


def builtin_to_boolean(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'toBoolean' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'toBoolean' expects a string.",
            node.line,
            node.column,
        )

    text = value.value.strip().lower()

    if text == "true":
        return BooleanValue(True)

    if text == "false":
        return BooleanValue(False)

    raise FunctionArgumentTypeError(
        "Invalid boolean conversion.",
        node.line,
        node.column,
    )