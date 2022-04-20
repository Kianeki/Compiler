import math
from Nodes import *

class OptimizationVisitor():
    def __init__(self, symbolTable):
        self.SymbolTable = symbolTable
        # Deze variabel geeft aan wanneer CP en CF geen nieuwe ast meer leveren
        # Elke keer CP of CF een verandering brengen zal hasChanged naar True veranderen zodat de while loop weet na
        # elke CP en CF combo dat er minstens 1 ding is aangepast in de AST om dan dit te blijven doen tot er
        # uiteindelijk False blijft op het einde van de combo
        self.hasChanged = True

# BELANGRIJK!!!
# MOMENTEEL ENKEL NODENUMBER CREATION VAN VARIABLE VALUE (TERWIJL DIT MOGELIJKS CHAR IS BV.) TODO LATER
    def ConstantPropagation(self, AST):
        if isinstance(AST, NodeAssignment):
            if isinstance(AST.RChild, NodeNumber):
            # MAG EIGENLIJK DE NODEVARIABLE ZIJN VALUE DIRECT VERANDEREN, MOET NIET DIE VAN IN DE SYMBOL TABLE ZIJN OMDAT DIE LINKED ZIJN AAN ELKAAR!
                self.SymbolTable.symbols[AST.LChild.identifier].value = AST.RChild.value
            else:
                AST.RChild = self.ConstantPropagation(AST.RChild)
            return AST
        elif isinstance(AST, NodeInfix):
            if isinstance(AST.LChild, NodeVariable):
                if self.SymbolTable.symbols[AST.LChild.identifier].value is not None:
                    AST.LChild = NodeNumber(self.SymbolTable.symbols[AST.LChild.identifier].value)
                    self.hasChanged = True
            if isinstance(AST.RChild, NodeVariable):
                if self.SymbolTable.symbols[AST.RChild.identifier].value is not None:
                    AST.RChild = NodeNumber(self.SymbolTable.symbols[AST.RChild.identifier].value)
                    self.hasChanged = True
            else:
                AST.LChild = self.ConstantPropagation(AST.LChild)
                AST.RChild = self.ConstantPropagation(AST.RChild)
            return AST
        elif isinstance(AST, NodeStart):
            for i in range(len(AST.nodes)):
                AST.nodes[i] = self.ConstantPropagation(AST.nodes[i])
        return AST

    def ConstantFolding(self, AST):
        if isinstance(AST, NodeUnary):
            if AST.sign == "+":
                self.hasChanged = True
                return NodeNumber(AST.child.value)
            else:
                self.hasChanged = True
                return NodeNumber(-AST.child.value)
        elif isinstance(AST, NodeAssignment):
            AST.RChild = self.ConstantFolding(AST.RChild)
            # self.SymbolTable.symbols[AST.LChild.identifier].value = self.ConstantFolding(AST.RChild).value
        elif isinstance(AST, NodeInfix):
            LChildLiteral = True
            RChildLiteral = True
            if not isinstance(AST.LChild, NodeNumber):
                AST.LChild = self.ConstantFolding(AST.LChild)
                if not isinstance(AST.LChild, NodeNumber):
                    LChildLiteral = False
            if not isinstance(AST.RChild, NodeNumber):
                AST.RChild = self.ConstantFolding(AST.RChild)
                if not isinstance(AST.RChild, NodeNumber):
                    RChildLiteral = False
            if LChildLiteral and RChildLiteral:
                self.hasChanged = True
                if isinstance(AST, NodePlus):
                    return NodeNumber(AST.LChild.value + AST.RChild.value)
                elif isinstance(AST, NodeMinus):
                    return NodeNumber(AST.LChild.value - AST.RChild.value)
                elif isinstance(AST, NodeMul):
                    return NodeNumber(AST.LChild.value * AST.RChild.value)
                elif isinstance(AST, NodeDiv):
                    if isinstance(AST.LChild.value, float) or isinstance(AST.RChild.value, float):
                        return NodeNumber(AST.LChild.value / AST.RChild.value)
                    else:
                        return NodeNumber(math.floor(AST.LChild.value / AST.RChild.value))

        elif isinstance(AST, NodeStart):
            for i in range(len(AST.nodes)):
                AST.nodes[i] = self.ConstantFolding(AST.nodes[i])
        return AST