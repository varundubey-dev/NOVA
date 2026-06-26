# Statistical Functions

Statistical functions perform common statistical calculations on numeric arrays.

All functions in this module require:

```nova
import stats
```

---

## stats.mean(array)

Returns the arithmetic mean of a numeric array.

### Parameters

| Name    | Type  | Description           |
| ------- | ----- | --------------------- |
| `array` | `[N]` | Source numeric array. |

### Returns

`N`

### Example

```nova
scores: [N] = [

    80,
    90,
    100

]

print(
    stats.mean(scores)
)
```

Output

```text
90
```

---

## stats.median(array)

Returns the median value of a numeric array.

### Parameters

| Name    | Type  | Description           |
| ------- | ----- | --------------------- |
| `array` | `[N]` | Source numeric array. |

### Returns

`N`

### Example

```nova
scores: [N] = [

    5,
    2,
    8,
    1,
    6

]

print(
    stats.median(scores)
)
```

Output

```text
5
```

---

## stats.mode(array)

Returns the most frequently occurring value in a numeric array.

### Parameters

| Name    | Type  | Description           |
| ------- | ----- | --------------------- |
| `array` | `[N]` | Source numeric array. |

### Returns

`N`

### Example

```nova
scores: [N] = [

    2,
    5,
    2,
    7,
    2,
    9

]

print(
    stats.mode(scores)
)
```

Output

```text
2
```

---

## stats.variance(array)

Returns the population variance of a numeric array.

### Parameters

| Name    | Type  | Description           |
| ------- | ----- | --------------------- |
| `array` | `[N]` | Source numeric array. |

### Returns

`N`

### Example

```nova
scores: [N] = [

    2,
    4,
    6,
    8

]

print(
    stats.variance(scores)
)
```

Example output

```text
5
```

---

## stats.stddev(array)

Returns the population standard deviation of a numeric array.

### Parameters

| Name    | Type  | Description           |
| ------- | ----- | --------------------- |
| `array` | `[N]` | Source numeric array. |

### Returns

`N`

### Example

```nova
scores: [N] = [

    2,
    4,
    6,
    8

]

print(
    stats.stddev(scores)
)
```

Example output

```text
2.236067977
```

The exact precision of the returned value is implementation-defined.