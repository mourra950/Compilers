from utils import *
from var import *
from statementsBody import *
from constpascal import *
def funcAndProcdBody(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Begin, indexPointer)
    Children.append(out1["node"])

    out2 = statements(out1["index"])
    Children.append(out2["node"])

    out3 = Match(Token_type.End, out2["index"])
    Children.append(out3["node"])

    out4 = Match(Token_type.Semicolon, out3["index"])
    Children.append(out4["node"])

    Node = Tree("funcAndProcdBody", Children)
    output["node"] = Node
    output["index"] = out4["index"]
    return output


def statements(indexPointer):
    Children = []
    output = dict()

    out1 = statement(indexPointer)
    Children.append(out1["node"])

    tempIndex = out1
    out2 = statementsDash(out1["index"])
    if out2:
        tempIndex = out2
        Children.append(out2["node"])

    Node = Tree("statements", Children)
    output["node"] = Node
    output["index"] = tempIndex["index"]
    return output

def statementsDash(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Semicolon, indexPointer, True)
    if str(out1)==';':
        Children.append(out1["node"])

        out2 = statement(out1["index"])
        Children.append(out2["node"])

        out3 = statementsDash(out2["index"])
        Children.append(out3["node"])

        Node = Tree("statementsDash", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output
    
    else:
        return

def statement(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Read, indexPointer, True)
    out2 = Match(Token_type.ReadLn, indexPointer, True)
    out3 = Match(Token_type.Write, indexPointer, True)
    out4 = Match(Token_type.WriteLn, indexPointer, True)
    out5 = Match(Token_type.If, indexPointer, True)
    out6 = Match(Token_type.For, indexPointer, True)
    out7 = Match(Token_type.Repeat, indexPointer, True)
    out8 = Match(Token_type.Identifier, indexPointer, True)
    out9 = varDecleration(indexPointer)
    out10 = constDecleration(indexPointer)
    tempIndex = indexPointer
    if str(out1["node"]) == 'READ':
        Children.append(out1["node"])

        match2 = Match(Token_type.OpenGroup, out1["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Identifier, match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        Children.append(match4["node"])
        tempIndex = match4
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(out2["node"]) == 'READLN':
        Children.append(out2["node"])

        match2 = Match(Token_type.OpenGroup, out2["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Identifier, match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        Children.append(match4["node"])
        tempIndex = match4
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(out3["node"]) == 'WRITE':
        Children.append(out3["node"])

        match2 = Match(Token_type.OpenGroup, out3["index"])
        Children.append(match2["node"])

        match3 = WriteArgument(match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        Children.append(match4["node"])
        tempIndex = match4
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(out4["node"]) == 'WRITELN':
        Children.append(out4["node"])

        match2 = Match(Token_type.OpenGroup, out4["index"])
        Children.append(match2["node"])

        match3 = WriteBody(match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        Children.append(match4["node"])
        tempIndex = match4
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(out5["node"]) == 'IF':
        Children.append(out5["node"])

        match2 = Condition(out5["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Then, match2["index"])
        Children.append(match3["node"])

        match4 = statements(match3["index"])
        Children.append(match4["node"])

        match5 = ElseClause(match4["index"])
        Children.append(match5["node"])
        tempIndex = match5
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(out6["node"]) == 'FOR':
        Children.append(out6["node"])

        match2 = Match(Token_type.Identifier, out6["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Assignment, match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.Integer, match3["index"])
        Children.append(match4["node"])

        match5 = Match(Token_type.To, match4["index"])
        Children.append(match5["node"])

        match6 = Match(Token_type.Integer, match5["index"])
        Children.append(match6["node"])

        match7 = Match(Token_type.Do, match6["index"])
        Children.append(match7["node"])

        match8 = statements(match7["index"])
        Children.append(match8["node"])
        tempIndex = match8
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(out7["node"]) == 'REPEAT':
        Children.append(out7["node"])

        match2 = statements(out7["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Until, match2["index"])
        Children.append(match3["node"])

        match4 = Condition(match3["index"])
        Children.append(match4["node"])
        tempIndex = match4
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(out8["node"])):
        Children.append(out8["node"])

        match2 = Match(Token_type.Assignment, out8["index"])
        Children.append(match2["node"])

        match3 = Expression(match2["index"])
        Children.append(match3["node"])
        tempIndex = match3
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif out9:
        if str(out9["node"]) != "(varDecleration ['error'])":
            Children.append(out9["node"])
            tempIndex = out9
            Node = Tree("statement", Children)
            output["node"] = Node
            output["index"] = tempIndex["index"]
            return output

    elif out10:
        if str(out10["node"]) != "(constDeleration ['error'])":
            Children.append(out10["node"])
            tempIndex = out10
            Node = Tree("statement", Children)
            output["node"] = Node
            output["index"] = tempIndex["index"]
            return output

    else:
        Node = Tree("statement", Children)
        output["node"] = "[error]"
        output["index"] = indexPointer + 1
        return output


