import time
from datetime import datetime

from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def builtin_now(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 0:
        raise FunctionArgumentCountError(
            f"Function 'now' expects 0 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    return StringValue(
        datetime.now().isoformat()
    )


def builtin_unix(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 0:
        raise FunctionArgumentCountError(
            f"Function 'unix' expects 0 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    return NumberValue(
        int(time.time())
    )


def builtin_timestamp(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 0:
        raise FunctionArgumentCountError(
            f"Function 'timestamp' expects 0 arguments, got {len(arguments)}.",
            node.line,
            node.column,
        )

    return NumberValue(
        time.time()
    )


def builtin_sleep(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'sleep' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    seconds = arguments[0]

    if not isinstance(seconds, NumberValue):
        raise FunctionArgumentTypeError(
            "Function 'sleep' expects a number.",
            node.line,
            node.column,
        )

    time.sleep(seconds.value)

    return None