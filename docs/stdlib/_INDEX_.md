# NOVA Standard Library

The NOVA Standard Library provides importable modules that extend the core language with additional functionality.

Unlike built-in functions, Standard Library modules must be explicitly imported before use.

---

## Importing Modules

Modules are imported using the `import` keyword.

```text
import math
```

Imported modules expose exported declarations through dot notation.

```text
math.sqrt(25)
```

---

## Library Modules

The Standard Library currently provides the following modules:

* [Mathematics](math.md)
* [Time](time.md)
* [Random](random.md)
* [Array](array.md)
* [Statistics](stats.md)

Additional modules will be introduced in future releases while maintaining backward compatibility.
