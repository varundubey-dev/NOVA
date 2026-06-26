# NOVA Language Specification

### Current Version (v1.0)

This document serves as the entry point for the current NOVA documentation.

NOVA v1.0 is the current stable release of the language.

Unlike traditional language specifications, the NOVA language specification is **incremental**. Each versioned specification documents the language features introduced in that release while building upon all previous versions. Together, these documents define the complete language.

---

# Language Specification

The complete NOVA language specification is distributed across the following documents.

Read them in version order.

| Version         | Features Introduced                                                 |
| --------------- | ------------------------------------------------------------------- |
| [v0.1](v0.1.md) | Core language, variables, arithmetic, output, comments              |
| [v0.2](v0.2.md) | Booleans, constants, null, any type, comparisons, logical operators |
| [v0.3](v0.3.md) | Arrays, typed arrays, nested arrays, array mutation                 |
| [v0.4](v0.4.md) | Schema maps, map instances, property access, structured data        |
| [v0.5](v0.5.md) | Conditionals, block scope, ternary expressions                      |
| [v0.6](v0.6.md) | Loops, ranges, array iteration, break, continue                     |
| [v0.7](v0.7.md) | User-defined functions, parameters, return values, recursion        |
| [v0.9](v0.9.md) | Modules, imports, exports, Standard Library modules                 |

---

# Built-in Functions

Built-in functions are globally available and do **not** require imports.

Documentation:

* [Built-in Functions Index](../builtins/_INDEX_.md)
* [Array Functions](../builtins/array.md)
* [String Functions](../builtins/string.md)
* [Type Conversion Functions](../builtins/conversions.md)
* [Input Functions](../builtins/input.md)

---

# Standard Library

The Standard Library provides reusable modules that are imported explicitly.

Documentation:

* [Standard Library Index](../stdlib/_INDEX_.md)
* [Mathematics Module](../stdlib/math.md)
* [Array Module](../stdlib/array.md)
* [Random Module](../stdlib/random.md)
* [Statistics Module](../stdlib/stats.md)
* [Time Module](../stdlib/time.md)

---

# Examples

Runnable example programs for every language release are available in:

* [Examples](../../examples/)

---

# Release Notes

Release notes describe the evolution of NOVA across versions.

* [NOVA v1.0.0 Release Notes](../releases/v1.0.0.md)
* [Changelog](../releases/_CHANGELOG_.md)

---

# Documentation Structure

| Documentation          | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| Language Specification | Incremental language syntax and grammar    |
| Built-in Functions     | Global functions available without imports |
| Standard Library       | Importable library modules                 |
| Examples               | Runnable example programs                  |
| Release Notes          | Version history and release summaries      |