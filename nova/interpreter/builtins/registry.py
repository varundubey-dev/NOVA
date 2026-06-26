from nova.interpreter.builtins.arrays import (
    builtin_length,
    builtin_push,
    builtin_pop,
    builtin_insert,
    builtin_remove,
    builtin_contains,
    builtin_clear,
)

from nova.interpreter.builtins.strings import (
    builtin_upper,
    builtin_lower,
    builtin_trim,
    builtin_starts_with,
    builtin_ends_with,
    builtin_replace,
    builtin_split,
)

from nova.interpreter.builtins.conversion import (
    builtin_to_boolean,
    builtin_to_number,
    builtin_to_string,
)

from nova.interpreter.builtins.intrinsic_math import (
    builtin_abs,
    builtin_ceil,
    builtin_floor,
    builtin_max,
    builtin_min,
    builtin_pow,
    builtin_round,
    builtin_sqrt,
)

from nova.interpreter.builtins.intrinsic_random import (
    builtin_random,
    builtin_randint,
    builtin_choice,
    builtin_shuffle,
    builtin_seed,
)

from nova.interpreter.builtins.intrinsic_time import (
    builtin_now,
    builtin_sleep,
    builtin_timestamp,
    builtin_unix,
)

from nova.interpreter.builtins.intrinsic_stats import (
    builtin_mean,
    builtin_median,
    builtin_mode,
    builtin_stddev,
    builtin_variance,
)

from nova.interpreter.builtins.intrinsic_array import (
    builtin_count,
    builtin_index_of,
    builtin_reverse,
    builtin_sort,
    builtin_unique,
)

from nova.interpreter.builtins.input import builtin_input

BUILTINS = {
    # Arrays
    "length": builtin_length,
    "push": builtin_push,
    "pop": builtin_pop,
    "insert": builtin_insert,
    "remove": builtin_remove,
    "contains": builtin_contains,
    "clear": builtin_clear,
    # Strings
    "upper": builtin_upper,
    "lower": builtin_lower,
    "trim": builtin_trim,
    "startsWith": builtin_starts_with,
    "endsWith": builtin_ends_with,
    "replace": builtin_replace,
    "split": builtin_split,
    # Conversion
    "toBoolean": builtin_to_boolean,
    "toNumber": builtin_to_number,
    "toString": builtin_to_string,
    # Input
    "input": builtin_input,
}

RUNTIME_INTRINSICS = {
    # Maths
    "abs": builtin_abs,
    "min": builtin_min,
    "max": builtin_max,
    "pow": builtin_pow,
    "sqrt": builtin_sqrt,
    "round": builtin_round,
    "floor": builtin_floor,
    "ceil": builtin_ceil,
    # Random
    "random": builtin_random,
    "randint": builtin_randint,
    "choice": builtin_choice,
    "shuffle": builtin_shuffle,
    "seed": builtin_seed,
    # Time
    "now": builtin_now,
    "sleep": builtin_sleep,
    "timestamp": builtin_timestamp,
    "unix": builtin_unix,
    # Stats
    "mean": builtin_mean,
    "median": builtin_median,
    "mode": builtin_mode,
    "stddev": builtin_stddev,
    "variance": builtin_variance,
    # Array
    "count": builtin_count,
    "indexOf": builtin_index_of,
    "reverse": builtin_reverse,
    "sort": builtin_sort,
    "unique": builtin_unique,
}
