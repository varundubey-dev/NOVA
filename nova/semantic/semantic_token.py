from dataclasses import dataclass


@dataclass(slots=True)
class SemanticToken:
    kind: str
    value: str
    line: int
    column: int
    length: int

    def to_dict(self):
        return {
            "kind": self.kind,
            "value": self.value,
            "line": self.line,
            "column": self.column,
            "length": self.length,
        }