from utils import *


def VarName(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = VarNameDash(out1["index"])
    if out2:
        out1 = out2
        Children.append(out2["node"])

    Node = Tree("VarName", Children)
    output["node"] = Node
    output["index"] = out1["index"]
    return output


def VarNameDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == ',':
        out1 = Match(Token_type.Comma, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = VarNameDash(out2["index"])
        if out3:
            out2 = out3
            Children.append(out3["node"])

        Node = Tree("VarNameDash", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return


def varDecleration1Dash(indexPointer):              # CHECK CODE AGAIN
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) in ReservedWords:
        return
    if re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)):
        out1 = VarName(indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Colon, out1["index"])
        Children.append(out2["node"])

        out3 = DataType(out2["index"])
        Children.append(out3["node"])

        out4 = Match(Token_type.Semicolon, out3["index"])
        Children.append(out4["node"])

        out5 = varDecleration1Dash(out4["index"])
        if out5:
            out4 = out5
            Children.append(out5["node"])

        Node = Tree("varDecleration1Dash", Children)
        output["node"] = Node
        output["index"] = out4["index"]
        return output
    else:
        return


def varDecleration1(indexPointer):
    Children = []
    output = dict()

    out1 = VarName(indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Colon, out1["index"])
    Children.append(out2["node"])

    out3 = DataType(out2["index"])
    Children.append(out3["node"])

    out4 = Match(Token_type.Semicolon, out3["index"])
    Children.append(out4["node"])

    out5 = varDecleration1Dash(out4["index"])
    if out5:
        out4 = out5
        Children.append(out5["node"])

    Node = Tree("varDecleration1", Children)
    output["node"] = Node
    output["index"] = out4["index"]
    return output


def varDecleration(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return

    if str(Tokens[indexPointer].lex) == 'VAR':
        out1 = Match(Token_type.Var, indexPointer)
        Children.append(out1["node"])

        out2 = varDecleration1(out1["index"])
        Children.append(out2["node"])

        Node = Tree("varDecleration", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return
