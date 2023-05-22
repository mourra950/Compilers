from pascaltokenizer import *
from pascaltokens import *


def Match(tokenmatch, index):
    newindex = index+1
    output = dict()

    if (index < len(Tokens)):
        Temp = Tokens[index].to_dict()
        if (Temp['token_type'] == tokenmatch):
            output["node"] = Temp['Lex']
            output["index"] = newindex
        else:
            output["node"] = ["error"]
            output["index"] = newindex 
            
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
    #print(str(Tokens[indexPointer].lex))

    if str(Tokens[indexPointer].lex) == "INTEGER":
        out7 = Match(Token_type.IntegerType, indexPointer)
        Children.append(out7["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out7["index"]

    elif str(Tokens[indexPointer].lex) == "REAL":
        out8 = Match(Token_type.RealType, indexPointer)
        Children.append(out8["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out8["index"]

    elif str(Tokens[indexPointer].lex) == "CHAR":
        out9 = Match(Token_type.CharType, indexPointer)
        Children.append(out9["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out9["index"]

    elif str(Tokens[indexPointer].lex) == "STRING":
        out10 = Match(Token_type.StringType, indexPointer)
        Children.append(out10["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out10["index"]

    elif str(Tokens[indexPointer].lex) == "BOOLEAN":
        out11 = Match(Token_type.BooleanType, indexPointer)
        Children.append(out11["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out11["index"]
        
    elif re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Int, indexPointer)
        Children.append(out1["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out1["index"]

    elif re.match("^[0-9].[0-9]$", str(Tokens[indexPointer].lex)):
        out2 = Match(Token_type.Real, indexPointer)
        Children.append(out2["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out2["index"]

    elif re.match("^[a-zA-Z]$", str(Tokens[indexPointer].lex)):
        out3 = Match(Token_type.Char, indexPointer)
        Children.append(out3["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out3["index"]

    elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)):
        out4 = Match(Token_type.Identifier, indexPointer)
        Children.append(out4["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out4["index"]

    elif re.match("^[TRUE | FALSE]$", str(Tokens[indexPointer].lex)):
        out5 = Match(Token_type.Boolean, indexPointer)
        Children.append(out5["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out5["index"]

    elif re.match('^".*"$', str(Tokens[indexPointer].lex)):
        out6 = Match(Token_type.Str, indexPointer)
        Children.append(out6["node"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = out6["index"]

   

    else:
        Children.append(["error"])
        Node = Tree("DataType", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1

    return output
