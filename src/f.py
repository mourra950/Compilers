from utils import *
from statements import *


def finalArgument(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Identifier, indexPointer, True)
    Children.append(out1["node"])

    out2 = Match(Token_type.Colon, indexPointer, True)
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

    out1 = Match(Token_type.Semicolon, indexPointer)
    if str(out1["node"]) == ';':
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
    if str(out1["node"]) != "(finalArgument ['error'])":
        Children.append(out1["node"])

        tempString = out1
        out2 = argumentDash(out1["index"])
        if out2:
            tempString = out2
            Children.append(out2["node"])
        
    else:
        tempString = out1
        out2 = argumentDash(out1["index"])
        if out2:
            tempString = out2
            Children.append(out2["node"])
    Node = Tree("argument", Children)
    output["node"] = Node
    output["index"] = tempString["index"]
    return output


def arguments(indexPointer):
    Children = []
    output = dict()

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


def functionDeclerationDash(indexPointer):
    Children = []
    output = dict()
    
    out1 = Match(Token_type.Function, indexPointer, True)
    if out1["node"] == "FUNCTION":
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = arguments(out2["index"])
        Children.append(out3["node"])

        out4 = Match(Token_type.Colon, out3["index"])
        Children.append(out4["node"])

        out5 = DataType(out4["index"])
        Children.append(out5["node"])

        out6 = Match(Token_type.Semicolon, out5["index"])
        Children.append(out6["node"])

        out7 = funcAndProcdBody(out6["index"])
        Children.append(out7["node"])

        tempIndex = out7
        out8 = functionDeclerationDash(out7["index"])
        if out8:
            tempIndex = out8
            Children.append(out8["node"])

        Node = Tree("functionDeclerationDash", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    else:  
        return



def FunctionDelaration(indexPointer):
    Children = []
    output = dict()
    
    out1 = Match(Token_type.Function, indexPointer, True)
    out1Temp =functionDeclerationDash(indexPointer)
    if out1["node"] == "FUNCTION":
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = arguments(out2["index"])
        Children.append(out3["node"])

        out4 = Match(Token_type.Colon, out3["index"])
        Children.append(out4["node"])

        out5 = DataType(out4["index"])
        Children.append(out5["node"])

        out6 = Match(Token_type.Semicolon, out5["index"])
        Children.append(out6["node"])

        out7 = funcAndProcdBody(out6["index"])
        Children.append(out7["node"])

        tempIndex = out7
        out8 = functionDeclerationDash(out7["index"])
        if out8:
            tempIndex = out8
            Children.append(out8["node"])

        Node = Tree("functionDecleration", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif out1Temp:
        if str(out1Temp["node"]) != "(functionDeclerationDash ['error'])":
            Children.append(out1["node"])

            Node = Tree("functionDecleration", Children)
            output["node"] = Node
            output["index"] = out1["index"]
            return output
    
    else:
        return
