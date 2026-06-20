import sys

from nova.lexer.lexer import Lexer
from nova.parser.parser import Parser
from nova.interpreter.interpreter import Interpreter


def run_file(path):
    with open(path, "r", encoding="utf-8") as file:
        source = file.read()

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    interpreter.interpret(ast)


def main():
    if len(sys.argv) != 2:
        print("Usage: nova <file.nova>")
        sys.exit(1)

    run_file(sys.argv[1])