# Random Functions

Random functions provide pseudo-random number generation and random operations on arrays.

All functions in this module require:

```nova
import random
```

---

## random.random()

Returns a pseudo-random number between `0.0` (inclusive) and `1.0` (exclusive).

### Parameters

None.

### Returns

`N`

### Example

```nova
print(
    random.random()
)
```

Example output

```text
0.4187312
```

The exact value returned is implementation-defined and will differ between calls.

---

## random.randint(min, max)

Returns a pseudo-random integer between the specified bounds (inclusive).

### Parameters

| Name  | Type | Description  |
| ----- | ---- | ------------ |
| `min` | `N`  | Lower bound. |
| `max` | `N`  | Upper bound. |

### Returns

`N`

### Example

```nova
print(
    random.randint(
        1,
        10
    )
)
```

Example output

```text
7
```

---

## random.choice(array)

Returns a randomly selected element from an array.

### Parameters

| Name    | Type  | Description   |
| ------- | ----- | ------------- |
| `array` | `[U]` | Source array. |

### Returns

`U`

### Example

```nova
names: [S] = [

    "Nova",
    "Orion",
    "Atlas"

]

print(
    random.choice(names)
)
```

Example output

```text
Orion
```

The selected element may differ between executions.

---

## random.shuffle(array)

Randomly shuffles the elements of an array in place.

### Parameters

| Name    | Type  | Description       |
| ------- | ----- | ----------------- |
| `array` | `[U]` | Array to shuffle. |

### Returns

`null`

### Example

```nova
numbers: [N] = [

    1,
    2,
    3,
    4,
    5

]

random.shuffle(numbers)

print(numbers)
```

Example output

```text
[3, 1, 5, 2, 4]
```

The shuffled order is implementation-defined and will differ between executions.

---

## random.seed(seed)

Initializes the pseudo-random number generator with the specified seed.

Using the same seed produces the same sequence of random values.

### Parameters

| Name   | Type | Description |
| ------ | ---- | ----------- |
| `seed` | `N`  | Seed value. |

### Returns

`null`

### Example

```nova
random.seed(42)

print(
    random.random()
)
```

Example output

```text
0.639426798
```

Using the same seed produces the same sequence of values across program executions.
