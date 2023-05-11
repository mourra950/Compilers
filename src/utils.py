from pascaltokenizer import *
from pascaltokens import *


def Match(tokenmatch, index,check=False):
    newindex = index+1
    output = dict()
    
    if (index < len(Tokens)):
        Temp = Tokens[index].to_dict()
        if (Temp['token_type'] == tokenmatch):
            output["node"] = Temp['Lex']
            output["index"] = newindex
        else:
            output["node"] = ["error"]
            output["index"] = index
            if not check:
                errors.append("Syntax error : " + 'token: "' +
                        Temp['Lex']+'" type: ' + str(tokenmatch))
        return output
    else:
        output["node"] = ["error"]
        output["index"] = newindex
        return output


def DataType(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Constant, indexPointer,True)
    out2 = Match(Token_type.Real, indexPointer,True)
    out3 = Match(Token_type.Char, indexPointer,True)
    out4 = Match(Token_type.Identifier, indexPointer,True)
    out5 = Match(Token_type.Boolean, indexPointer,True)

    if re.match("^[0-9]*$", str(out1["node"])):
        Children.append(out1["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out1["index"]

    elif re.match("^[0-9].[0-9]$", str(out2["node"])):
        Children.append(out2["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out2["index"]

    elif re.match("^[a-zA-Z]$", str(out3["node"])):
        Children.append(out3["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out3["index"]

    elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(out4["node"])):
        Children.append(out4["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out4["index"]

    elif re.match("^[TRUE | FALSE]$", str(out5["node"])):
        Children.append(out5["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out5["index"]
    return output
