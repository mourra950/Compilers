from utils import *


def LibrarySection(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Uses, indexPointer)
    Children.append(out1["node"])

    out2 = Library(out1["index"])
    Children.append(out2["node"])

    out3 = Match(Token_type.Semicolon, out2["index"])
    Children.append(out3["node"])

    Node = Tree("LibrarySection", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output


def Library(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = LibraryDash(out1["index"])
    if out2:
        Children.append(out2["node"])

    Node = Tree("Library", Children)
    output["node"] = Node
    output["index"] = out2["index"]
    return output


def LibraryDash(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Comma, indexPointer)
    if (str(out1["node"]) == ','):
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = LibraryDash(out2["index"])
        if out3:
            out2 = out3
            Children.append(out3["node"])

        Node = Tree("LibraryDash", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        if errors:
            errors.pop()
        return
