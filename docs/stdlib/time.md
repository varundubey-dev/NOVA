# Time Functions

Time functions provide access to the system clock and execution timing.

All functions in this module require:

```nova
import time
```

---

## time.now()

Returns the current local date and time as a formatted string.

### Parameters

None.

### Returns

`S`

### Example

```nova
print(
    time.now()
)
```

Example output

```text
2026-06-26 18:42:11
```

---

## time.unix()

Returns the current Unix timestamp.

### Parameters

None.

### Returns

`N`

### Example

```nova
print(
    time.unix()
)
```

Example output

```text
1782505371
```

---

## time.timestamp()

Returns the current Unix timestamp.

This function is equivalent to `time.unix()`.

### Parameters

None.

### Returns

`N`

### Example

```nova
print(
    time.timestamp()
)
```

Example output

```text
1782505371
```

---

## time.sleep(seconds)

Pauses program execution for the specified number of seconds.

### Parameters

| Name      | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| `seconds` | `N`  | Number of seconds to pause execution. |

### Returns

`null`

### Example

```nova
print("Starting")

time.sleep(2)

print("Finished")
```

Example output

```text
Starting
Finished
```

Program execution is paused for approximately two seconds between the two output statements.