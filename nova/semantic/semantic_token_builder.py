from nova.ast import (
    Program,
    VariableDeclaration,
    ConstantDeclaration,
    FunctionDeclaration,
    Parameter,
    Assignment,
    ArrayAssignment,
    SchemaDeclaration,
    PropertyAssignment,
    ReturnStatement,
    PrintStatement,
    BlockStatement,
    IfStatement,
    WhileStatement,
    ForRangeStatement,
    ForEachStatement,
    BreakStatement,
    ContinueStatement,
    ImportStatement,
    ImportItem,
    Identifier,
    ArrayAccess,
    PropertyAccess,
    BinaryExpression,
    UnaryExpression,
    TernaryExpression,
    FunctionCall,
    NumberLiteral,
    StringLiteral,
    BooleanLiteral,
    NullLiteral,
    ArrayLiteral,
    MapEntry,
    MapLiteral,
    ArrayType,
    SchemaField,
    SchemaType,
)
from nova.semantic.semantic_token import SemanticToken


class SemanticTokenBuilder:
    def __init__(self):
        self.tokens: list[SemanticToken] = []

    def build(self, program):
        self.tokens.clear()

        self.visit(program)

        return self.tokens

    def emit(self, kind, node, value):
        self.tokens.append(
            SemanticToken(
                kind=kind,
                value=value,
                line=node.line,
                column=node.column,
                length=len(value),
            )
        )

    def visit(self, node):
        if node is None:
            return

        method = getattr(
            self,
            f"visit_{type(node).__name__}",
            self.generic_visit,
        )

        method(node)

    def generic_visit(self, node):
        pass

    def visit_Program(self, node: Program):
        for statement in node.statements:
            self.visit(statement)

    def visit_BlockStatement(self, node: BlockStatement):
        for statement in node.statements:
            self.visit(statement)

    def visit_FunctionDeclaration(self, node: FunctionDeclaration):
        self.emit("FUNCTION", node, node.name)

        for parameter in node.parameters:
            self.visit(parameter)

        self.visit(node.body)

    def visit_Parameter(self, node: Parameter):
        self.emit("PARAMETER", node, node.name)

    def visit_VariableDeclaration(self, node: VariableDeclaration):
        self.emit("VARIABLE", node, node.name)

        self.visit(node.value)

    def visit_ConstantDeclaration(self, node: ConstantDeclaration):
        self.emit("CONSTANT", node, node.name)

        self.visit(node.value)

    def visit_SchemaDeclaration(self, node: SchemaDeclaration):
        self.emit("SCHEMA", node, node.name)

        self.visit(node.schema)

    def visit_ImportStatement(self, node: ImportStatement):
        self.emit("MODULE", node, node.module_path)

        if node.imports:
            for item in node.imports:
                self.visit(item)

    def visit_ImportItem(self, node: ImportItem):
        self.emit("MODULE_MEMBER", node, node.name)

    def visit_Assignment(self, node: Assignment):
        self.visit(node.value)

    def visit_ArrayAssignment(self, node: ArrayAssignment):
        self.visit(node.target)
        self.visit(node.value)

    def visit_PropertyAssignment(self, node: PropertyAssignment):
        self.visit(node.target)
        self.visit(node.value)

    def visit_ReturnStatement(self, node: ReturnStatement):
        self.visit(node.value)

    def visit_PrintStatement(self, node: PrintStatement):
        for expression in node.expressions:
            self.visit(expression)

    def visit_IfStatement(self, node: IfStatement):
        self.visit(node.condition)
        self.visit(node.then_branch)
        self.visit(node.else_branch)

    def visit_WhileStatement(self, node: WhileStatement):
        self.visit(node.condition)
        self.visit(node.body)

    def visit_ForRangeStatement(self, node: ForRangeStatement):
        self.emit("VARIABLE", node, node.variable_name)

        self.visit(node.start)
        self.visit(node.end)
        self.visit(node.body)

    def visit_ForEachStatement(self, node: ForEachStatement):
        self.emit("VARIABLE", node, node.variable_name)

        self.visit(node.iterable)
        self.visit(node.body)

    def visit_FunctionCall(self, node: FunctionCall):
        if isinstance(node.callee, Identifier):
            self.emit(
                "FUNCTION",
                node.callee,
                node.callee.name,
            )
        else:
            self.visit(node.callee)

        for argument in node.arguments:
            self.visit(argument)

    def visit_BreakStatement(self, node: BreakStatement):
        pass

    def visit_ContinueStatement(self, node: ContinueStatement):
        pass

    def visit_Identifier(self, node: Identifier):
        pass

    def visit_ArrayAccess(self, node: ArrayAccess):
        self.visit(node.array)
        self.visit(node.index)

    def visit_PropertyAccess(self, node: PropertyAccess):
        self.visit(node.target)

    def visit_BinaryExpression(self, node: BinaryExpression):
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryExpression(self, node: UnaryExpression):
        self.visit(node.operand)

    def visit_TernaryExpression(self, node: TernaryExpression):
        self.visit(node.condition)
        self.visit(node.true_expression)
        self.visit(node.false_expression)

    def visit_NumberLiteral(self, node: NumberLiteral):
        pass

    def visit_StringLiteral(self, node: StringLiteral):
        pass

    def visit_BooleanLiteral(self, node: BooleanLiteral):
        pass

    def visit_NullLiteral(self, node: NullLiteral):
        pass

    def visit_ArrayLiteral(self, node: ArrayLiteral):
        for element in node.elements:
            self.visit(element)

    def visit_MapEntry(self, node: MapEntry):
        self.visit(node.value)

    def visit_MapLiteral(self, node: MapLiteral):
        for entry in node.entries:
            self.visit(entry)

    def visit_ArrayType(self, node: ArrayType):
        for element_type in node.element_types:
            self.visit(element_type)

    def visit_SchemaField(self, node: SchemaField):
        self.visit(node.field_type)

    def visit_SchemaType(self, node: SchemaType):
        for field in node.fields:
            self.visit(field)
