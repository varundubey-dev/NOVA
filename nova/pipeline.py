from nova.lexer.lexer import Lexer
from nova.lexer.token_types import TokenType
from nova.parser.parser import Parser
from nova.interpreter.interpreter import Interpreter


def create_interpreter(
    source: str,
    input_provider=None,
    resolver=None,
    is_stdlib=False,
    output_callback=None,
):
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser_tokens = [token for token in tokens if token.type != TokenType.COMMENT]

    parser = Parser(parser_tokens)
    ast = parser.parse()

    interpreter = Interpreter(
        input_provider=input_provider,
        resolver=resolver,
        is_stdlib=is_stdlib,
        output_callback=output_callback,
    )

    interpreter.interpret(ast)

    return interpreter
