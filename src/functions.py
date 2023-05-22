from utils import *
from statements import *
from var import *

def finalArgument(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Colon, out1["index"])
    Children.append(out2["node"])

    out3 = DataType(out2["index"])
    Children.append(out3["node"])

    Node = Tree("finalArgument", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output


def argumentDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
   
    if str(Tokens[indexPointer].lex) == ';':
        out1 = Match(Token_type.Semicolon, indexPointer)
        Children.append(out1["node"])

        out2 = finalArgument(out1["index"])
        Children.append(out2["node"])
    
        tempIndex = out2
        out3 = argumentDash(out2["index"])
        if out3:
            tempIndex = out3
            Children.append(out3["node"])

        Node = Tree("argumentDash", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output
    
    else:
        return



def argument(indexPointer):
    Children = []
    output = dict()

    out1 = finalArgument(indexPointer)      
    Children.append(out1["node"])           # I want to append the error if it happens
    tempNode = out1
    out2 = argumentDash(out1["index"])
    if out2:
        tempNode = out2
        Children.append(out2["node"])
    Node = Tree("argument", Children)
    output["node"] = Node
    output["index"] = tempNode["index"]
    return output
    

def arguments(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == '(':
        out1 = Match(Token_type.OpenGroup, indexPointer)
        Children.append(out1["node"])

        out2 = argument(out1["index"])

        Children.append(out2["node"])

        out3 = Match(Token_type.CloseGroup, out2["index"])
        Children.append(out3["node"])

        Node = Tree("arguments", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output
    else:
        return


def functionDeclerationDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == 'FUNCTION':
        
        out1 = Match(Token_type.Function, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        tempNode = out2
        out3 = arguments(tempNode["index"])
        if out3:
            tempNode = out3
            Children.append(out3["node"])

        out4 = returnStatement(tempNode["index"])
        if out4:
            tempNode = out4
            Children.append(out4["node"])

        out5 = Match(Token_type.Semicolon, tempNode["index"])
        Children.append(out5["node"])
        tempNode = out5
        
        out6 = varDecleration(out5["index"])
        if out6:
            tempNode = out6
            Children.append(out6["node"])

        out7 = funcAndProcdBody(tempNode["index"])
        Children.append(out7["node"])

        tempNode = out7
        out8 = functionDeclerationDash(tempNode["index"])
        if out8:
            tempNode = out8
            Children.append(out8["node"])

        Node = Tree("functionDeclerationDash", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    

    else:  
        return



def FunctionDelaration(indexPointer):       
    Children = []
    output = dict()

    

    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == 'FUNCTION':
        
        out1 = Match(Token_type.Function, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        tempNode = out2
        out3 = arguments(tempNode["index"])
        if out3:
            tempNode = out3
            Children.append(out3["node"])

        out4 = returnStatement(tempNode["index"])
        if out4:
            tempNode = out4
            Children.append(out4["node"])

        out5 = Match(Token_type.Semicolon, tempNode["index"])
        Children.append(out5["node"])
        tempNode = out5
        
        out6 = varDecleration(out5["index"])
        if out6:
            tempNode = out6
            Children.append(out6["node"])

        out7 = funcAndProcdBody(tempNode["index"])
        Children.append(out7["node"])

        tempNode = out7
        out8 = functionDeclerationDash(tempNode["index"])
        if out8:
            tempNode = out8
            Children.append(out8["node"])

        Node = Tree("functionDeclerationDash", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    else:
        tempIndex = indexPointer
        out1Temp =functionDeclerationDash(indexPointer)
        if out1Temp:
            tempIndex = out1Temp["index"]
            Children.append(out1Temp["node"])
        Node = Tree("functionDecleration", Children)
        output["node"] = Node
        output["index"] = tempIndex
        return output
    


def returnStatement(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == ':':
        out1 = Match(Token_type.Colon, indexPointer)
        Children.append(out1["node"])

        out2 = DataType(out1["index"])
        Children.append(out2["node"])


        Node = Tree("returnStatement", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return