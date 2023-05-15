from utils import *


def constDecleration(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Const, indexPointer)
    if (str(out1["node"]) == 'CONST'):
        Children.append(out1["node"])

        out2 = ConstName(out1["index"])
        Children.append(out2["node"])

        Node = Tree("constDeleration", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        if errors:
            errors.pop()
        return


def ConstName(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Equal, out1["index"])
    Children.append(out2["node"])

    out3 = Match(Token_type.Constant, out2["index"])
    Children.append(out3["node"])

    out4 = Match(Token_type.Semicolon, out3["index"])
    Children.append(out4["node"])

    out5 = ConstNameDash(out4["index"])
    if out5:
        out4 = out5
        Children.append(out5["node"])

    Node = Tree("ConstName", Children)
    output["node"] = Node
    output["index"] = out4["index"]
    return output


def ConstNameDash(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Identifier, indexPointer, True)

    if re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(out1["node"])):
        Children.append(out1["node"])

        out2 = Match(Token_type.Equal, out1["index"])
        Children.append(out2["node"])

        out3 = Match(Token_type.Constant, out2["index"])
        Children.append(out3["node"])

        out4 = Match(Token_type.Semicolon, out3["index"])
        Children.append(out4["node"])

        out5 = ConstNameDash(out4["index"])
        if out5:
            out4 = out5
            Children.append(out5["node"])

        Node = Tree("ConstNameDash", Children)
        output["node"] = Node
        output["index"] = out4["index"]
        return output
    else:
        return

