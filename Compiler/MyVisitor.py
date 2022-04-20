from calcVisitor import calcVisitor
from calcParser import calcParser

from Nodes import *


class SymbolTable():
    def __init__(self, ParentSymbolTable = None):
        self.symbols = {}
        self.ParentSymbolTable = ParentSymbolTable

class ASTBuilder(calcVisitor):
    def __init__(self):
        self.SymbolTable = SymbolTable()

    def visitStart(self, ctx:calcParser.StartContext):
        node = NodeStart()
        for child in ctx.getChildren():
            node.nodes.append(child.accept(self))
        while None in node.nodes:
            node.nodes.remove(None)
        return node

    def visitNumber(self, ctx:calcParser.NumberContext):
        content = ctx.getText()
        if content.find(".") != -1:
            return NodeNumber(float(content))
        else:
            return NodeNumber(int(content))

    def visitParenthesesExp(self, ctx:calcParser.ParenthesesExpContext):
        if ctx.getChildCount() == 3:
            return ctx.getChild(1).accept(self)
        else:
            node = NodeUnary(ctx.getChild(0).getText(), ctx.getChild(2).accept(self))
            return node

    def visitInfixExp(self, ctx:calcParser.InfixExpContext):
        operation = ctx.getChild(1).getText()
        if operation == "+":
            return NodePlus(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))
        elif operation == "-":
            return NodeMinus(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))
        elif operation == "*":
            return NodeMul(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))
        elif operation == "/":
            return NodeDiv(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))

    def visitAssignment(self, ctx:calcParser.AssignmentContext):
        return NodeAssignment(ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))

    def visitDeclaration(self, ctx:calcParser.DeclarationContext):
        node = NodeVariable(ctx.getChild(0).getText(), ctx.getChild(1).getText())
        self.SymbolTable.symbols[node.identifier] = node
        return node

    def visitVadExp(self, ctx:calcParser.VadExpContext):
        if ctx.getChild(0).getRuleIndex() == 9:
            varName = ctx.getChild(0).getText()
            return self.SymbolTable.symbols[varName]
        else:
            return ctx.getChild(0).accept(self)

    def visitPrintf(self, ctx:calcParser.PrintfContext):
        return NodePrintf(ctx.getChild(2).getText())
