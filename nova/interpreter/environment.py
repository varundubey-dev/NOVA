from nova.interpreter.runtime_values import (
    NumberValue,
    StringValue,
)


class Environment:
    def __init__(self):
        self.variables = {}

    def validate_type(self, expected_type, value):
        if value is None:
            return

        if expected_type == "N":
            if not isinstance(value, NumberValue):
                raise Exception("Datatype mismatch.")

        elif expected_type == "S":
            if not isinstance(value, StringValue):
                raise Exception("Datatype mismatch.")

    def declare_variable(self, name, var_type, value=None):
        if name in self.variables:
            raise Exception(f"Variable '{name}' already declared.")

        self.validate_type(var_type, value)

        self.variables[name] = {
            "type": var_type,
            "value": value,
            "initialized": value is not None,
        }

    def assign_variable(self, name, value):
        if name not in self.variables:
            raise Exception(f"Variable '{name}' is not declared.")

        variable = self.variables[name]

        self.validate_type(variable["type"], value)

        variable["value"] = value
        variable["initialized"] = True

    def get_variable(self, name):
        if name not in self.variables:
            raise Exception(f"Variable '{name}' is not declared.")

        variable = self.variables[name]

        if not variable["initialized"]:
            raise Exception(f"Variable '{name}' accessed before initialization.")

        return variable["value"]
