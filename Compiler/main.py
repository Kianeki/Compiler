import sys
from antlr4 import *
from calcLexer import calcLexer
from calcParser import calcParser
from MyVisitor import ASTBuilder
from Optimizer import OptimizationVisitor
from LLVM import LLVMGenerator

# class EvaluateExpressionVisitor:
#     def visit(self, node):
#         if type(node) == ExpressionNode:
#             if node.value == "+":
#                 return self.visit(node.left) + self.visit(node.right)
#             elif node.value == "-":
#                 return self.visit(node.left) - self.visit(node.right)
#             elif node.value == "*":
#                 return self.visit(node.left) * self.visit(node.right)
#             elif node.value == "/":
#                 return self.visit(node.left) / self.visit(node.right)
#             else:
#                 return node.value
#     def visitNumber(self, ctx: calcParser.NumberContext):
#         return NumberNode(value=int(str(ctx.INT())))
#     def visitExperssion(self, ctx: calcParser.ExpressionContext):
#         node = ExpressionNode()
#         if ctx.PLUS():
#             node.value = "+"
#         elif ctx.MINUS():
#             node.value = "-"
#         elif ctx.MUL():
#             node.value = "*"
#         elif ctx.DIV():
#             node.value = "/"



def toDot(AST, count):
    string = "digraph G {\n"
    string += dotCalc(AST, 0)[0]
    string += "}"
    dotFile = open("dotFile" + str(count) + '.dot', "w")
    dotFile.write(string)
    dotFile.close()


def dotCalc(AST, count):
    string = str(count) + ' [label="' + AST.whatAmI() + '"];\n'
    myCount = count
    for child in AST.getNodes():
        string += str(myCount) + ' -> ' + str(count + 1) + '\n'
        tup = dotCalc(child, count + 1)
        string += tup[0]
        count = tup[1]
    return string, count


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = calcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = calcParser(stream)
    tree = parser.start()
    ast_builder = ASTBuilder()
    AST = ast_builder.visitStart(tree)
    toDot(AST, 0)
    optimizer = OptimizationVisitor(ast_builder.SymbolTable)
    while optimizer.hasChanged is True:
        optimizer.hasChanged = False
        AST = optimizer.ConstantPropagation(AST)
        AST = optimizer.ConstantFolding(AST)
    toDot(AST, 1)
    codeGenerator = LLVMGenerator(ast_builder.SymbolTable)
    codeGenerator.toLLVM(AST, 0)


if __name__ == '__main__':
    main(sys.argv)
