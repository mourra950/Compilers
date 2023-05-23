from utils import *
from statementsFile import *
from var import *


def WriteBody(indexPointer):
    Children = []
    output = dict()

    out1 = WriteArgument(indexPointer)
    Children.append(out1["node"])

    out2 = WriteBodyDash(out1["index"])
    if out2:
        out1 = out2
        Children.append(out2["node"])

    Node = Tree("WriteBody", Children)
    output["node"] = Node
    output["index"] = out1["index"]
    return output


def WriteBodyDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    
    if str(Tokens[indexPointer].lex) == ',':
        out1 = Match(Token_type.Comma, indexPointer)
        Children.append(out1["node"])

        out2 = WriteArgument(out1["index"])
        Children.append(out2["node"])

        tempIndex = out2
        out3 = WriteBodyDash(out2["index"])
        if out3:
            tempIndex = out3
            Children.append(out3["node"])

        Node = Tree("WriteBodyDash", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    else:
        return


def WriteArgument(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if re.match('^".*"$', str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Str, indexPointer)
        Children.append(out1["node"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)):
        out2 = Match(Token_type.Identifier, indexPointer)
        Children.append(out2["node"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    else:
        Children.append(["error"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def ExpressionDash(indexPointer):
    Children = []
    output = dict()

    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == '+' or str(Tokens[indexPointer].lex) == '-':
        out1 = AddOp(indexPointer)
        Children.append(out1["node"])

        out2 = Term(out1["index"])
        Children.append(out2["node"])

        tempIndex = out2
        out3 = ExpressionDash(out2["index"])
        if out3:
            tempIndex = out3
            Children.append(out3["node"])

        Node = Tree("ExpressionDash", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output
    else:
        return


def Expression(indexPointer):
    Children = []
    output = dict()

    out1 = Term(indexPointer)
    Children.append(out1["node"])
    tempIndex = out1

    out2 = ExpressionDash(out1["index"])
    if out2:
        tempIndex = out2
        Children.append(out2["node"])

    Node = Tree("Expression", Children)
    output["node"] = Node
    output["index"] = tempIndex["index"]
    return output


def Condition(indexPointer):
    Children = []
    output = dict()

    out1 = Expression(indexPointer)
    Children.append(out1["node"])

    out2 = RelOp(out1["index"])
    Children.append(out2["node"])

    out3 = Expression(out2["index"])
    Children.append(out3["node"])

    Node = Tree("Condition", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output


def Term(indexPointer):
    Children = []
    output = dict()

    out1 = Factor(indexPointer)
    Children.append(out1["node"])

    tempIndex = out1
    out2 = TermDash(out1["index"])
    if out2:
        tempIndex = out2
        Children.append(out2["node"])

    Node = Tree("Term", Children)
    output["node"] = Node
    output["index"] = tempIndex["index"]
    return output


def TermDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    
    if str(Tokens[indexPointer].lex) == '*' or str(Tokens[indexPointer].lex) == '/':
        out1 = MultOp(indexPointer)
        Children.append(out1["node"])

        out2 = Factor(out1["index"])
        Children.append(out2["node"])

        tempIndex = out2
        out3 = TermDash(out2["index"])
        if out3:
            tempIndex = out3
            Children.append(out3["node"])

        Node = Tree("TermDash", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    else:
        return


def Factor(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    
    if re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Identifier, indexPointer)
        Children.append(out1["node"])
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output
    elif re.match("^[0-9].[0-9]$", str(Tokens[indexPointer].lex)) or re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out2 = Constant(indexPointer)
        Children.append(out2["node"])
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    
    else: 
        Children.append(["error"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def RelOp(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == "<=":
        out1 = Match(Token_type.LessEqual, indexPointer)
        Children.append(out1["node"])
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif str(Tokens[indexPointer].lex) == ">=":
        out2 = Match(Token_type.GreatEqual, indexPointer)
        Children.append(out2["node"])
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "=":
        out3 = Match(Token_type.Equal, indexPointer)
        Children.append(out3["node"])
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output

    elif str(Tokens[indexPointer].lex) == ">":
        out4 = Match(Token_type.Greater, indexPointer)
        Children.append(out4["node"])
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = out4["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "<":
        out5 = Match(Token_type.Lesser, indexPointer)
        Children.append(out5["node"])
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = out5["index"]
        return output
    
    else:
        Children.append(["error"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output

    


def AddOp(indexPointer):
    Children = []
    output = dict()

    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == "+":
        out1 = Match(Token_type.PlusOp, indexPointer)
        Children.append(out1["node"])
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "-":
        out2 = Match(Token_type.MinusOp, indexPointer)
        Children.append(out2["node"])
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    else:
        Children.append(["error"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def MultOp(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == "*":
        out1 = Match(Token_type.MultiplyOp, indexPointer)
        Children.append(out1["node"])
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "/":
        out2 = Match(Token_type.DivideOp, indexPointer)
        Children.append(out2["node"])
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    else:
        Children.append(["error"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output





def Constant(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Int, indexPointer)
        Children.append(out1["node"])
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif re.match("^[0-9].[0-9]$", str(Tokens[indexPointer].lex)):
        out2 = Match(Token_type.Real, indexPointer)
        Children.append(out2["node"])
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    else:
        Children.append(["error"])
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def ForBody(indexPointer):
    return