from utils import *

def WriteBody(indexPointer):
    Children = []
    output = dict()

    out1 = WriteArgument(indexPointer)
    Children.append(out1["node"])

    out2 = writeBodyDash(out1["index"])
    Children.append(out2["node"])

    out3 = Match(Token_type.End, out2["index"])
    Children.append(out3["node"])

    out4 = Match(Token_type.Semicolon, out3["index"])
    Children.append(out4["node"])

    Node = Tree("Header", Children)
    output["node"] = Node
    output["index"] = out4["index"]
    return output