from utils import *
def constDecleration(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == 'CONST':
        out1 = Match(Token_type.Const, indexPointer)
        Children.append(out1["node"])

        out2 = ConstName(out1["index"])
        Children.append(out2["node"])
        Node = Tree("constDeleration", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return


def ConstName(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Equal, out1["index"])
    Children.append(out2["node"])

    out3 = Constant(out2["index"])
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
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) in ReservedWords:
           return
    if re.match("^[a-zA-Z][a-zA-Z0-9_]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Identifier, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Equal, out1["index"])
        Children.append(out2["node"])

        out3 = Constant(out2["index"])
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

def Constant(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    if re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Int, indexPointer)
        Children.append(out1["node"])
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif re.match("^[0-9]+\.[0-9]+$", str(Tokens[indexPointer].lex)):
        out2 = Match(Token_type.Real, indexPointer)
        Children.append(out2["node"])
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    else:
        Children.append(["error"])
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("Constant", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
