from enum import Enum, auto


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()
    NULL = auto()

    # Identifiers
    IDENTIFIER = auto()

    # Keywords
    PRINT = auto()

    # Datatypes
    TYPE = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    MODULO = auto()

    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()

    LESS = auto()
    GREATER = auto()

    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()

    AND = auto()
    OR = auto()
    NOT = auto()

    # Symbols
    COLON = auto()
    DOUBLE_COLON = auto()
    EQUALS = auto()

    LPAREN = auto()
    RPAREN = auto()

    # Special
    NEWLINE = auto()
    EOF = auto()
