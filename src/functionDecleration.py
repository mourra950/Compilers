from utils import *
from functionDecleration import *
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

    Node = Tree("Header", Children)
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

        Node = Tree("Header", Children)
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

        out2 = argumentDash(out1["index"])
        Children.append(out2["node"])
        
    else:
        out2 = argumentDash(indexPointer)
        Children.append(out2["node"])

    Node = Tree("Header", Children)
    output["node"] = Node
    output["index"] = out2["index"]
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

    Node = Tree("Header", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output


def functionDeclerationDash(indexPointer):
    Children = []
    output = dict()
    
    out1 = Match(Token_type.Function, indexPointer, True)
    if out1:
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

        Node = Tree("Header", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    else:  
        return


def functionDecleration(indexPointer):
    Children = []
    output = dict()
    
    out1 = Match(Token_type.Function, indexPointer, True)
    if out1:
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

        Node = Tree("Header", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    else:
        out1 =functionDeclerationDash(indexPointer)
        Children.append(out1["node"])

        Node = Tree("Header", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output


    