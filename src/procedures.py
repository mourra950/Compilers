from statements import *
from utils import *
from functions import *
from var import *

def procedureDecleration(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == 'PROCEDURE':
        out1 = Match(Token_type.Procedure, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = arguments(out2["index"])
        if out3:
            out2 = out3
            Children.append(out3["node"])

        out4 = Match(Token_type.Semicolon, out2["index"])
        Children.append(out4["node"])
        tempNode = out4
        out5 = varDecleration(out4["index"])
        if out5:
            tempNode = out5
            Children.append(out5["node"])

        out6 = funcAndProcdBody(tempNode["index"])
        Children.append(out6["node"])
        tempNode = out6
        out7 = procedureDeclerationDash(out6["index"])
        if out7:
            tempNode = out7
            Children.append(out7["node"])

        Node = Tree("procedureDecleration", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    else:
        tempIndex = indexPointer
        out1 = procedureDeclerationDash(indexPointer)
        if out1:
            tempIndex = out1["index"]
            Children.append(out1["node"])
        Node = Tree("procedureDecleration", Children)
        output["node"] = Node
        output["index"] = tempIndex
        return output
    

def procedureDeclerationDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == 'PROCEDURE':
        out1 = Match(Token_type.Procedure, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = arguments(out2["index"])
        if out3:
            out2 = out3
            Children.append(out3["node"])

        out4 = Match(Token_type.Semicolon, out2["index"])
        Children.append(out4["node"])
        tempNode = out4
        out5 = varDecleration(out4["index"])
        if out5:
            tempNode = out5
            Children.append(out5["node"])

        out6 = funcAndProcdBody(tempNode["index"])
        Children.append(out6["node"])
        tempNode = out6
        out7 = procedureDeclerationDash(out6["index"])
        if out7:
            tempNode = out7
            Children.append(out7["node"])

        Node = Tree("procedureDecleration", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    else:
        return
    

def execution(indexPointer):
    Children = []
    output = dict()
    
    out1 = Match(Token_type.Begin, indexPointer)
    Children.append(out1["node"])

    out2 = statements(out1["index"])
    if out2:
        out1 = out2
        Children.append(out2["node"])

    out3 = Match(Token_type.EndProgram, out1["index"])
    Children.append(out3["node"])

    Node = Tree("execution", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output
