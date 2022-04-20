from Nodes import *

class LLVMGenerator():
    def __init__(self, symbolTable):
        self.SymbolTable = symbolTable

    def toLLVM(self, AST, count):
        llvmFile = open("llvmFile" + str(count) + '.ll', "w")
        text = self.LLVMVisitor(AST)
        llvmFile.write(text)
        llvmFile.close()

    def LLVMVisitor(self, AST):
        text = "define dso_local i32 @main(){\n"
        rcount = 1
        potentialLoadQueue = []
        for node in AST.nodes:
            if isinstance(node, NodeAssignment):
                node.LChild.storageNumber = rcount
                potentialLoadQueue.append(rcount)
                text += "%" + str(rcount) + " = alloca "
                if node.LChild.reserved == "int":
                    text += "i32, align 4\n"
                    text += "store i32 " + str(node.LChild.value) + ", i32* %" + str(rcount) + ", align 4\n"
                elif node.LChild.reserved == "float":
                    text += "float, align 4\n"
                    text += "store float " + str(node.LChild.value) + ", float* %" + str(rcount) + ", align 4\n"
                elif node.LChild.reserved == "char":
                    text += "i8, align 1\n"
                    text += "store i8 " + str(node.LChild.value) + ", i8* %" + str(rcount) + ", align 1\n"
            rcount += 1
        text += "ret i32 0\n}"
        return text
