# Generated from calc.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete generic visitor for a parse tree produced by calcParser.

class calcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calcParser#start.
    def visitStart(self, ctx:calcParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#numberExp.
    def visitNumberExp(self, ctx:calcParser.NumberExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#vadExp.
    def visitVadExp(self, ctx:calcParser.VadExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#unaryExp.
    def visitUnaryExp(self, ctx:calcParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#parenthesesExp.
    def visitParenthesesExp(self, ctx:calcParser.ParenthesesExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#printExp.
    def visitPrintExp(self, ctx:calcParser.PrintExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#infixExp.
    def visitInfixExp(self, ctx:calcParser.InfixExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#relogicExp.
    def visitRelogicExp(self, ctx:calcParser.RelogicExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#printf.
    def visitPrintf(self, ctx:calcParser.PrintfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#pointer.
    def visitPointer(self, ctx:calcParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#declaration.
    def visitDeclaration(self, ctx:calcParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#assignment.
    def visitAssignment(self, ctx:calcParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#relOperation.
    def visitRelOperation(self, ctx:calcParser.RelOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#logicOperation.
    def visitLogicOperation(self, ctx:calcParser.LogicOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#unaryOperation.
    def visitUnaryOperation(self, ctx:calcParser.UnaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#var.
    def visitVar(self, ctx:calcParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#number.
    def visitNumber(self, ctx:calcParser.NumberContext):
        return self.visitChildren(ctx)



del calcParser