# Generated from calc.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete listener for a parse tree produced by calcParser.
class calcListener(ParseTreeListener):

    # Enter a parse tree produced by calcParser#start.
    def enterStart(self, ctx:calcParser.StartContext):
        pass

    # Exit a parse tree produced by calcParser#start.
    def exitStart(self, ctx:calcParser.StartContext):
        pass


    # Enter a parse tree produced by calcParser#numberExp.
    def enterNumberExp(self, ctx:calcParser.NumberExpContext):
        pass

    # Exit a parse tree produced by calcParser#numberExp.
    def exitNumberExp(self, ctx:calcParser.NumberExpContext):
        pass


    # Enter a parse tree produced by calcParser#vadExp.
    def enterVadExp(self, ctx:calcParser.VadExpContext):
        pass

    # Exit a parse tree produced by calcParser#vadExp.
    def exitVadExp(self, ctx:calcParser.VadExpContext):
        pass


    # Enter a parse tree produced by calcParser#unaryExp.
    def enterUnaryExp(self, ctx:calcParser.UnaryExpContext):
        pass

    # Exit a parse tree produced by calcParser#unaryExp.
    def exitUnaryExp(self, ctx:calcParser.UnaryExpContext):
        pass


    # Enter a parse tree produced by calcParser#parenthesesExp.
    def enterParenthesesExp(self, ctx:calcParser.ParenthesesExpContext):
        pass

    # Exit a parse tree produced by calcParser#parenthesesExp.
    def exitParenthesesExp(self, ctx:calcParser.ParenthesesExpContext):
        pass


    # Enter a parse tree produced by calcParser#printExp.
    def enterPrintExp(self, ctx:calcParser.PrintExpContext):
        pass

    # Exit a parse tree produced by calcParser#printExp.
    def exitPrintExp(self, ctx:calcParser.PrintExpContext):
        pass


    # Enter a parse tree produced by calcParser#infixExp.
    def enterInfixExp(self, ctx:calcParser.InfixExpContext):
        pass

    # Exit a parse tree produced by calcParser#infixExp.
    def exitInfixExp(self, ctx:calcParser.InfixExpContext):
        pass


    # Enter a parse tree produced by calcParser#relogicExp.
    def enterRelogicExp(self, ctx:calcParser.RelogicExpContext):
        pass

    # Exit a parse tree produced by calcParser#relogicExp.
    def exitRelogicExp(self, ctx:calcParser.RelogicExpContext):
        pass


    # Enter a parse tree produced by calcParser#printf.
    def enterPrintf(self, ctx:calcParser.PrintfContext):
        pass

    # Exit a parse tree produced by calcParser#printf.
    def exitPrintf(self, ctx:calcParser.PrintfContext):
        pass


    # Enter a parse tree produced by calcParser#pointer.
    def enterPointer(self, ctx:calcParser.PointerContext):
        pass

    # Exit a parse tree produced by calcParser#pointer.
    def exitPointer(self, ctx:calcParser.PointerContext):
        pass


    # Enter a parse tree produced by calcParser#declaration.
    def enterDeclaration(self, ctx:calcParser.DeclarationContext):
        pass

    # Exit a parse tree produced by calcParser#declaration.
    def exitDeclaration(self, ctx:calcParser.DeclarationContext):
        pass


    # Enter a parse tree produced by calcParser#assignment.
    def enterAssignment(self, ctx:calcParser.AssignmentContext):
        pass

    # Exit a parse tree produced by calcParser#assignment.
    def exitAssignment(self, ctx:calcParser.AssignmentContext):
        pass


    # Enter a parse tree produced by calcParser#relOperation.
    def enterRelOperation(self, ctx:calcParser.RelOperationContext):
        pass

    # Exit a parse tree produced by calcParser#relOperation.
    def exitRelOperation(self, ctx:calcParser.RelOperationContext):
        pass


    # Enter a parse tree produced by calcParser#logicOperation.
    def enterLogicOperation(self, ctx:calcParser.LogicOperationContext):
        pass

    # Exit a parse tree produced by calcParser#logicOperation.
    def exitLogicOperation(self, ctx:calcParser.LogicOperationContext):
        pass


    # Enter a parse tree produced by calcParser#unaryOperation.
    def enterUnaryOperation(self, ctx:calcParser.UnaryOperationContext):
        pass

    # Exit a parse tree produced by calcParser#unaryOperation.
    def exitUnaryOperation(self, ctx:calcParser.UnaryOperationContext):
        pass


    # Enter a parse tree produced by calcParser#var.
    def enterVar(self, ctx:calcParser.VarContext):
        pass

    # Exit a parse tree produced by calcParser#var.
    def exitVar(self, ctx:calcParser.VarContext):
        pass


    # Enter a parse tree produced by calcParser#number.
    def enterNumber(self, ctx:calcParser.NumberContext):
        pass

    # Exit a parse tree produced by calcParser#number.
    def exitNumber(self, ctx:calcParser.NumberContext):
        pass



del calcParser