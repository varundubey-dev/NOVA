# Array Functions

Array functions provide common algorithms for sorting, searching, and manipulating arrays.

All functions in this module require:

```nova
import array
```

---

## array.sort(array)

Sorts an array in ascending order.

### Parameters

| Name    | Type  | Description    |
| ------- | ----- | -------------- |
| `array` | `[U]` | Array to sort. |

### Returns

`null`

### Example

```nova
numbers: [N] = [

    5,
    2,
    8,
    1

]

array.sort(numbers)

print(numbers)
```

Output

```text
[1, 2, 5, 8]
```

---

## array.reverse(array)

Reverses the elements of an array in place.

### Parameters

| Name    | Type  | Description       |
| ------- | ----- | ----------------- |
| `array` | `[U]` | Array to reverse. |

### Returns

`null`

### Example

```nova
numbers: [N] = [

    1,
    2,
    3,
    4

]

array.reverse(numbers)

print(numbers)
```

Output

```text
[4, 3, 2, 1]
```

---

## array.unique(array)

Returns a new array containing only the first occurrence of each element.

### Parameters

| Name    | Type  | Description   |
| ------- | ----- | ------------- |
| `array` | `[U]` | Source array. |

### Returns

`[U]`

### Example

```nova
numbers: [N] = [

    1,
    2,
    2,
    3,
    3,
    4

]

print(
    array.unique(numbers)
)
```

Output

```text
[1, 2, 3, 4]
```

---

## array.count(array, value)

Returns the number of occurrences of a value in an array.

### Parameters

| Name    | Type  | Description     |
| ------- | ----- | --------------- |
| `array` | `[U]` | Source array.   |
| `value` | `U`   | Value to count. |

### Returns

`N`

### Example

```nova
numbers: [N] = [

    1,
    2,
    2,
    3,
    2

]

print(
    array.count(
        numbers,
        2
    )
)
```

Output

```text
3
```

---

## array.indexOf(array, value)

Returns the index of the first occurrence of a value.

Returns `-1` if the value is not found.

### Parameters

| Name    | Type  | Description      |
| ------- | ----- | ---------------- |
| `array` | `[U]` | Source array.    |
| `value` | `U`   | Value to locate. |

### Returns

`N`

### Example

```nova
numbers: [N] = [

    10,
    20,
    30,
    40

]

print(
    array.indexOf(
        numbers,
        30
    )
)
```

Output

```text
2
```

If the value does not exist:

```text
-1
```
