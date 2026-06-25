from nova.interpreter.runtime_values import (
    StringValue,
    BooleanValue,
    ArrayValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_upper(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'upper' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'upper' expects a string.",
            node.line,
            node.column,
        )

    return StringValue(value.value.upper())


def builtin_lower(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'lower' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'lower' expects a string.",
            node.line,
            node.column,
        )

    return StringValue(value.value.lower())


def builtin_trim(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'trim' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    value = arguments[0]

    if not isinstance(value, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'trim' expects a string.",
            node.line,
            node.column,
        )

    return StringValue(value.value.strip())


def builtin_starts_with(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'startsWith' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    string = arguments[0]
    prefix = arguments[1]

    if not isinstance(string, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'startsWith' expects a string as the first argument.",
            node.line,
            node.column,
        )

    if not isinstance(prefix, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'startsWith' expects a string as the second argument.",
            node.line,
            node.column,
        )

    return BooleanValue(
        string.value.startswith(prefix.value)
    )


def builtin_ends_with(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'endsWith' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    string = arguments[0]
    suffix = arguments[1]

    if not isinstance(string, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'endsWith' expects a string as the first argument.",
            node.line,
            node.column,
        )

    if not isinstance(suffix, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'endsWith' expects a string as the second argument.",
            node.line,
            node.column,
        )

    return BooleanValue(
        string.value.endswith(suffix.value)
    )


def builtin_replace(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 3:
        raise FunctionArgumentCountError(
            f"Function 'replace' expects 3 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    string = arguments[0]
    old = arguments[1]
    new = arguments[2]

    if not isinstance(string, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'replace' expects a string as the first argument.",
            node.line,
            node.column,
        )

    if not isinstance(old, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'replace' expects a string as the second argument.",
            node.line,
            node.column,
        )

    if not isinstance(new, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'replace' expects a string as the third argument.",
            node.line,
            node.column,
        )

    return StringValue(
        string.value.replace(
            old.value,
            new.value,
        )
    )


def builtin_split(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 2:
        raise FunctionArgumentCountError(
            f"Function 'split' expects 2 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    string = arguments[0]
    delimiter = arguments[1]

    if not isinstance(string, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'split' expects a string as the first argument.",
            node.line,
            node.column,
        )

    if not isinstance(delimiter, StringValue):
        raise FunctionArgumentTypeError(
            "Function 'split' expects a string as the second argument.",
            node.line,
            node.column,
        )

    return ArrayValue(
        [
            StringValue(part)
            for part in string.value.split(delimiter.value)
        ]
    )