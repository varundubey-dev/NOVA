import statistics

from nova.interpreter.runtime_values import (
    NumberValue,
    ArrayValue,
)

from nova.errors import (
    FunctionArgumentCountError,
    FunctionArgumentTypeError,
)


def require_numeric_array(
    value,
    node,
    function_name,
):
    if not isinstance(value, ArrayValue):
        raise FunctionArgumentTypeError(
            f"Function '{function_name}' expects an array.",
            node.line,
            node.column,
        )

    if len(value.value) == 0:
        raise FunctionArgumentTypeError(
            f"Function '{function_name}' cannot operate on an empty array.",
            node.line,
            node.column,
        )

    numbers = []

    for element in value.value:
        if not isinstance(element, NumberValue):
            raise FunctionArgumentTypeError(
                f"Function '{function_name}' expects an array of numbers.",
                node.line,
                node.column,
            )

        numbers.append(element.value)

    return numbers


def builtin_mean(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'mean' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = require_numeric_array(
        arguments[0],
        node,
        "mean",
    )

    return NumberValue(statistics.mean(values))


def builtin_median(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'median' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = require_numeric_array(
        arguments[0],
        node,
        "median",
    )

    return NumberValue(statistics.median(values))


def builtin_mode(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'mode' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = require_numeric_array(
        arguments[0],
        node,
        "mode",
    )

    try:
        result = statistics.mode(values)

    except statistics.StatisticsError:
        raise FunctionArgumentTypeError(
            "No unique mode exists.",
            node.line,
            node.column,
        )

    return NumberValue(result)


def builtin_variance(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'variance' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = require_numeric_array(
        arguments[0],
        node,
        "variance",
    )

    return NumberValue(
        statistics.pvariance(values)
    )


def builtin_stddev(
    interpreter,
    argument_nodes,
    arguments,
    node,
):
    if len(arguments) != 1:
        raise FunctionArgumentCountError(
            f"Function 'stddev' expects 1 argument, got {len(arguments)}.",
            node.line,
            node.column,
        )

    values = require_numeric_array(
        arguments[0],
        node,
        "stddev",
    )

    return NumberValue(
        statistics.pstdev(values)
    )