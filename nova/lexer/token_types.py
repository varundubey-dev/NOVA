from enum import Enum, auto


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()

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

    # Symbols
    COLON = auto()
    EQUALS = auto()

    LPAREN = auto()
    RPAREN = auto()

    # Special
    NEWLINE = auto()
    EOF = auto()
