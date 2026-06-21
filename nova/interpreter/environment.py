from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
    BooleanValue,
    NullValue,
    ArrayValue,
)

from nova.parser.ast_nodes import ArrayType


class Environment:
    def __init__(self):
        self.variables = {}

    def validate_type(self, expected_type, value):
        if value is None:
            return

        if isinstance(value, NullValue):
            return

        # Primitive Any
        if expected_type == "U":
            return

        # Primitive Types
        if expected_type == "N":
            if not isinstance(value, NumberValue):
                raise Exception("Datatype mismatch.")
            return

        if expected_type == "S":
            if not isinstance(value, StringValue):
                raise Exception("Datatype mismatch.")
            return

        if expected_type == "B":
            if not isinstance(value, BooleanValue):
                raise Exception("Datatype mismatch.")
            return

        # Array Types
        if isinstance(expected_type, ArrayType):
            if not isinstance(value, ArrayValue):
                raise Exception("Datatype mismatch.")

            allowed_types = expected_type.element_types

            for element in value.value:
                valid = False

                for allowed_type in allowed_types:
                    try:
                        self.validate_type(
                            allowed_type,
                            element,
                        )
                        valid = True
                        break

                    except Exception:
                        pass

                if not valid:
                    raise Exception("Invalid datatype inside array.")

            return

        raise Exception(f"Unknown datatype '{expected_type}'.")

    def declare_variable(self, name, var_type, value=None):
        if name in self.variables:
            raise Exception(f"Variable '{name}' already declared.")

        self.validate_type(var_type, value)

        self.variables[name] = {
            "type": var_type,
            "value": value,
            "initialized": value is not None,
            "constant": False,
        }

    def declare_constant(self, name, const_type, value=None):
        if name in self.variables:
            raise Exception(f"Variable '{name}' already declared.")

        self.validate_type(const_type, value)

        self.variables[name] = {
            "type": const_type,
            "value": value,
            "initialized": value is not None,
            "constant": True,
        }

    def assign_variable(self, name, value):
        if name not in self.variables:
            raise Exception(f"Variable '{name}' is not declared.")

        variable = self.variables[name]

        if variable["constant"] and variable["initialized"]:
            raise Exception("Cannot reassign immutable variable.")

        self.validate_type(
            variable["type"],
            value,
        )

        variable["value"] = value
        variable["initialized"] = True
        
    def get_variable_info(self, name):
        if name not in self.variables:
            raise Exception(
                f"Variable '{name}' is not declared."
            )

        return self.variables[name]

    def get_variable(self, name):
        if name not in self.variables:
            raise Exception(f"Variable '{name}' is not declared.")

        variable = self.variables[name]

        if not variable["initialized"]:
            raise Exception(f"Variable '{name}' accessed before initialization.")

        return variable["value"]
