from utils import *
from var import *
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

    tempIndex = indexPointer
    out1 = statement(indexPointer)
    if out1:
        tempIndex = out1["index"]
        Children.append(out1["node"])

    
    out2 = statementsDash(tempIndex)
    if out2:
        tempIndex = out2["index"]
        Children.append(out2["node"])

    Node = Tree("statements", Children)
    output["node"] = Node
    output["index"] = tempIndex
    return output

def statementsDash(indexPointer):
    Children = []
    output = dict()

    
    out1 = statement(indexPointer)
    
    if out1:
        Children.append(out1["node"])
        tempNode = out1
        out2 = statementsDash(out1["index"])
        
        if out2:
            tempNode = out2
            Children.append(out2["node"])

        Node = Tree("statementsDash", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    
    else:
        return

def statement(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    
    tempIndex = indexPointer
    
    if str(Tokens[indexPointer].lex) == "READ":
        out1 = Match(Token_type.Read, indexPointer)
        Children.append(out1["node"])

        match2 = Match(Token_type.OpenGroup, out1["index"])
        match2["node"] = match2["node"].replace("(", "OpenBracket")
        Children.append(match2["node"])

        match3 = Match(Token_type.Identifier, match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        match4["node"] = match4["node"].replace(")", "ClosedBracket")
        Children.append(match4["node"])
        

        match5 = Match(Token_type.Semicolon, match4["index"])
        Children.append(match5["node"])
        tempIndex = match5
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "READLN":
        out2 = Match(Token_type.ReadLn, indexPointer)
        Children.append(out2["node"])

        match2 = Match(Token_type.OpenGroup, out2["index"])
        match2["node"] = match2["node"].replace("(", "OpenBracket")
        Children.append(match2["node"])

        match3 = Match(Token_type.Identifier, match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        match4["node"] = match4["node"].replace(")", "ClosedBracket")
        Children.append(match4["node"])
        
        match5 = Match(Token_type.Semicolon, match4["index"])
        Children.append(match5["node"])
        tempIndex = match5
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "WRITE":
        out3 = Match(Token_type.Write, indexPointer)
        Children.append(out3["node"])

        match2 = Match(Token_type.OpenGroup, out3["index"])
        match2["node"] = match2["node"].replace("(", "OpenBracket")
        Children.append(match2["node"])

        match3 = WriteBody(match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        match4["node"] = match4["node"].replace(")", "ClosedBracket")
        Children.append(match4["node"])
        
        match5 = Match(Token_type.Semicolon, match4["index"])
        Children.append(match5["node"])
        tempIndex = match5
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "WRITELN":
        out4 = Match(Token_type.WriteLn, indexPointer)
        Children.append(out4["node"])

        match2 = Match(Token_type.OpenGroup, out4["index"])
        match2["node"] = match2["node"].replace("(", "OpenBracket")
        Children.append(match2["node"])

        match3 = WriteBody(match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.CloseGroup, match3["index"])
        match4["node"] = match4["node"].replace(")", "ClosedBracket")
        Children.append(match4["node"])
        
        match5 = Match(Token_type.Semicolon, match4["index"])
        Children.append(match5["node"])
        tempIndex = match5
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "IF":
        out5 = Match(Token_type.If, indexPointer)
        Children.append(out5["node"])

        match2 = Condition(out5["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Then, match2["index"])
        Children.append(match3["node"])

        match4 = statements(match3["index"])
        Children.append(match4["node"])

        tempIndex = match4
        match5 = ElseClause(match4["index"])
        if match5:
            tempIndex = match5
            Children.append(match5["node"])

        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "FOR":
        out6 = Match(Token_type.For, indexPointer)
        Children.append(out6["node"])

        match2 = Match(Token_type.Identifier, out6["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Assignment, match2["index"])
        Children.append(match3["node"])

        match4 = Match(Token_type.Int, match3["index"])
        Children.append(match4["node"])

        match5 = Match(Token_type.To, match4["index"])
        Children.append(match5["node"])

        match6 = ToStatment(match5["index"])
        Children.append(match6["node"])

        match7 = Match(Token_type.Do, match6["index"])
        Children.append(match7["node"])

        match8 = ForBody(match7["index"])
        Children.append(match8["node"])

        tempIndex = match8
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    
    elif str(Tokens[indexPointer].lex) == "REPEAT":
        out7 = Match(Token_type.Repeat, indexPointer)
        Children.append(out7["node"])

        match2 = statements(out7["index"])
        Children.append(match2["node"])

        match3 = Match(Token_type.Until, match2["index"])
        Children.append(match3["node"])

        match4 = Condition(match3["index"])
        Children.append(match4["node"])
        
        match5 = Match(Token_type.Semicolon, match4["index"])
        Children.append(match5["node"])
        tempIndex = match5
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "VAR":
        out9 = varDecleration(indexPointer)
        Children.append(out9["node"])
        tempIndex = out9
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output

    elif str(Tokens[indexPointer].lex) == "CONST":
        out10 = constDecleration(indexPointer)
        Children.append(out10["node"])
        tempIndex = out10
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output
    
    elif str(Tokens[indexPointer].lex) in ReservedWords:
        return
    
    elif (str(Tokens[indexPointer+1].lex) == "(" or str(Tokens[indexPointer+1].lex) == ";") and re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)):
        out11 = FunctionAndProcedureCall(indexPointer)
        Children.append(out11["node"])

        out12 = Match(Token_type.Semicolon, out11["index"])
        Children.append(out12["node"])

        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = out12["index"]
        return output
    
    elif re.match("^[a-zA-Z][a-zA-Z0-9_]*$", str(Tokens[indexPointer].lex)):
        out8 = Match(Token_type.Identifier, indexPointer)
        Children.append(out8["node"])

        match2 = Match(Token_type.Assignment, out8["index"])
        Children.append(match2["node"])

        match3 = AssignedStatement(match2["index"])
        Children.append(match3["node"])
        
        match4 = Match(Token_type.Semicolon, match3["index"])
        Children.append(match4["node"])
        tempIndex = match4
        Node = Tree("statement", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output


    else:
        return 


def ElseClause(indexPointer):
    Children = []
    output = dict()

    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == "ELSE":
        out1 = Match(Token_type.Else, indexPointer)
        Children.append(out1["node"])

        out2 = statements(out1["index"])
        Children.append(out2["node"])

        Node = Tree("ElseClause", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    else:
        return
    
def ForBody(indexPointer):
    Children = []
    output = dict()
    
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == "BEGIN":
        out1 = Match(Token_type.Begin, indexPointer)
        Children.append(out1["node"])

        out2 = statements(out1["index"])
        if out2:
            out1 = out2
            Children.append(out2["node"])

        out3 = Match(Token_type.End, out1["index"])
        Children.append(out3["node"])
        
        out4 = Match(Token_type.Semicolon, out3["index"])
        Children.append(out4["node"])

        Node = Tree("ForBody", Children)
        output["node"] = Node
        output["index"] = out4["index"]
        return output
    else:
        tempIndex = indexPointer
        out1 = statement(indexPointer)
        if out1:
            tempIndex = out1["index"]
            Children.append(out1["node"])
            Node = Tree("ForBody", Children)
            output["node"] = Node
            output["index"] = tempIndex
            return output
        else:
            Children.append(["error"])
            errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
            Node = Tree("ForBody", Children)
            output["node"] = Node
            output["index"] = indexPointer + 1
            return output

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
    if len(Tokens) <= indexPointer + 1:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    if re.match("^'.*'$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Str, indexPointer)
        Children.append(out1["node"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif str(Tokens[indexPointer+1].lex) == '(':
        out2 = FunctionAndProcedureCall(indexPointer)
        Children.append(out2["node"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output        

    elif re.match("^[a-zA-Z][a-zA-Z0-9_]*$", str(Tokens[indexPointer].lex)):
        out3 = Match(Token_type.Identifier, indexPointer)
        Children.append(out3["node"])
        Node = Tree("WriteArgument", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output

    else:
        Children.append(["error"])
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
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

    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("Condition", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    
    if str(Tokens[indexPointer].lex) == '(':
        out1 = Match(Token_type.OpenGroup, indexPointer)
        out1["node"] = out1["node"].replace("(", "OpenBracket")
        Children.append(out1["node"])

        out2 = Expression(out1["index"])
        Children.append(out2["node"])

        out3 = RelOp(out2["index"])
        Children.append(out3["node"])

        out4 = Expression(out3["index"])
        Children.append(out4["node"])

        out5 = Match(Token_type.CloseGroup, out4["index"])
        out5["node"] = out5["node"].replace(")", "ClosedBracket")
        Children.append(out5["node"])

        Node = Tree("Condition", Children)
        output["node"] = Node
        output["index"] = out5["index"]
        return output
    
    else:
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
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    
    if re.match("^[a-zA-Z][a-zA-Z0-9_]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Identifier, indexPointer)
        Children.append(out1["node"])
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output
    elif re.match("^[0-9]+\.[0-9]+$", str(Tokens[indexPointer].lex)) or re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out2 = Constant(indexPointer)
        Children.append(out2["node"])
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    
    else: 
        Children.append(["error"])
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("Factor", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def RelOp(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
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
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("RelOp", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output

    


def AddOp(indexPointer):
    Children = []
    output = dict()

    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
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
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("AddOp", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def MultOp(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
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
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("MultOp", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output


def FunctionAndProcedureCall(indexPointer):
    Children = []
    output = dict()


    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = FunctionAndProcedureCallArgument(out1["index"])
    if out2:
        out1 = out2
        Children.append(out2["node"])

    Node = Tree("FunctionAndProcedureCall", Children)
    output["node"] = Node
    output["index"] = out1["index"]
    return output

def AssignedStatement(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer+1:       # We lookahead one index after to see if we find ( or ; to check for function call against expression
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("AssignedStatement", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    if (str(Tokens[indexPointer+1].lex) == "(" or str(Tokens[indexPointer+1].lex) == ";") and re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)):
        out1 = FunctionAndProcedureCall(indexPointer)
        Children.append(out1["node"])
        Node = Tree("AssignedStatement", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output

    elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(Tokens[indexPointer].lex)) or re.match("^[0-9]+\.[0-9]+$", str(Tokens[indexPointer].lex)) or re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out2 = Expression(indexPointer)
        Children.append(out2["node"])
        Node = Tree("AssignedStatement", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output

    elif re.match("^'.*'$", str(Tokens[indexPointer].lex)):
        out2 = Match(Token_type.Str, indexPointer)
        Children.append(out2["node"])
        Node = Tree("AssignedStatement", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        Children.append(["error"])
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("AssignedStatement", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    
def finalArgument(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Colon, out1["index"])
    Children.append(out2["node"])

    out3 = DataType(out2["index"])
    Children.append(out3["node"])

    Node = Tree("finalArgument", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output


def argumentDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
   
    if str(Tokens[indexPointer].lex) == ';':
        out1 = Match(Token_type.Semicolon, indexPointer)
        Children.append(out1["node"])

        out2 = finalArgument(out1["index"])
        Children.append(out2["node"])
    
        tempIndex = out2
        out3 = argumentDash(out2["index"])
        if out3:
            tempIndex = out3
            Children.append(out3["node"])

        Node = Tree("argumentDash", Children)
        output["node"] = Node
        output["index"] = tempIndex["index"]
        return output
    
    else:
        return



def argument(indexPointer):
    Children = []
    output = dict()

    out1 = finalArgument(indexPointer)      
    Children.append(out1["node"])           # I want to append the error if it happens
    tempNode = out1
    out2 = argumentDash(out1["index"])
    if out2:
        tempNode = out2
        Children.append(out2["node"])
    Node = Tree("argument", Children)
    output["node"] = Node
    output["index"] = tempNode["index"]
    return output
    

def arguments(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == '(':
        out1 = Match(Token_type.OpenGroup, indexPointer)
        out1["node"] = out1["node"].replace("(", "OpenBracket")
        Children.append(out1["node"])

        out2 = argument(out1["index"])

        Children.append(out2["node"])

        out3 = Match(Token_type.CloseGroup, out2["index"])
        out3["node"] = out3["node"].replace(")", "ClosedBracket")
        Children.append(out3["node"])

        Node = Tree("arguments", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output
    else:
        return


def functionDeclarationDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == 'FUNCTION':
        
        out1 = Match(Token_type.Function, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        tempNode = out2
        out3 = arguments(tempNode["index"])
        if out3:
            tempNode = out3
            Children.append(out3["node"])

        out4 = returnStatement(tempNode["index"])
        if out4:
            tempNode = out4
            Children.append(out4["node"])

        out5 = Match(Token_type.Semicolon, tempNode["index"])
        Children.append(out5["node"])
        tempNode = out5
        
        out6 = varDecleration(out5["index"])
        if out6:
            tempNode = out6
            Children.append(out6["node"])

        out7 = funcAndProcdBody(tempNode["index"])
        Children.append(out7["node"])

        tempNode = out7
        out8 = functionDeclarationDash(tempNode["index"])
        if out8:
            tempNode = out8
            Children.append(out8["node"])

        Node = Tree("functionDeclarationDash", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    

    else:  
        return



def FunctionDeclaration(indexPointer):       
    Children = []
    output = dict()

    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("FunctionDeclaration", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    if str(Tokens[indexPointer].lex) == 'FUNCTION':
        
        out1 = Match(Token_type.Function, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        tempNode = out2
        out3 = arguments(tempNode["index"])
        if out3:
            tempNode = out3
            Children.append(out3["node"])

        out4 = returnStatement(tempNode["index"])
        if out4:
            tempNode = out4
            Children.append(out4["node"])

        out5 = Match(Token_type.Semicolon, tempNode["index"])
        Children.append(out5["node"])
        tempNode = out5
        
        out6 = varDecleration(out5["index"])
        if out6:
            tempNode = out6
            Children.append(out6["node"])

        out7 = funcAndProcdBody(tempNode["index"])
        Children.append(out7["node"])

        tempNode = out7
        out8 = functionDeclarationDash(tempNode["index"])
        if out8:
            tempNode = out8
            Children.append(out8["node"])

        Node = Tree("FunctionDeclaration", Children)
        output["node"] = Node
        output["index"] = tempNode["index"]
        return output
    else:
        tempIndex = indexPointer
        out1Temp =functionDeclarationDash(indexPointer)
        if out1Temp:
            tempIndex = out1Temp["index"]
            Children.append(out1Temp["node"])
        Node = Tree("FunctionDeclaration", Children)
        output["node"] = Node
        output["index"] = tempIndex
        return output
    


def returnStatement(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == ':':
        out1 = Match(Token_type.Colon, indexPointer)
        Children.append(out1["node"])

        out2 = DataType(out1["index"])
        Children.append(out2["node"])


        Node = Tree("returnStatement", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return
    
def FunctionAndProcedureCallArgument(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == '(':
        out1 = Match(Token_type.OpenGroup, indexPointer)
        out1["node"] = out1["node"].replace("(", "OpenBracket")
        Children.append(out1["node"])

        out2 = FunctionArgument(out1["index"])
        Children.append(out2["node"])

        out3 = Match(Token_type.CloseGroup, out2["index"])
        out3["node"] = out3["node"].replace(")", "ClosedBracket")
        Children.append(out3["node"])


        Node = Tree("FunctionAndProcedureCallArgument", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output
    else:
        return

def ToStatment(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        Children.append(["error"])
        errors.append("Syntax error")
        Node = Tree("ToStatment", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    if re.match("^[a-zA-Z][a-zA-Z0-9_]*$", str(Tokens[indexPointer].lex)):
        out1 = Match(Token_type.Identifier, indexPointer)
        Children.append(out1["node"])

        Node = Tree("ToStatment", Children)
        output["node"] = Node
        output["index"] = out1["index"]
        return output
    
    elif re.match("^[0-9]*$", str(Tokens[indexPointer].lex)):
        out2 = Match(Token_type.Int, indexPointer)
        Children.append(out2["node"])

        Node = Tree("ToStatment", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    
    else:
        Children.append(["error"])
        errors.append("Syntax error : " + 'token: "' + Tokens[indexPointer].lex +'" type: ' + str(Tokens[indexPointer].token_type))
        Node = Tree("ToStatment", Children)
        output["node"] = Node
        output["index"] = indexPointer + 1
        return output
    
def FunctionArgument(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = FunctionArgumentDash(out1["index"])
    if out2:
        out1 = out2
        Children.append(out2["node"])

    Node = Tree("FunctionArgument", Children)
    output["node"] = Node
    output["index"] = out1["index"]
    return output

def FunctionArgumentDash(indexPointer):
    Children = []
    output = dict()
    if len(Tokens) <= indexPointer:
        return
    if str(Tokens[indexPointer].lex) == ',':
        out1 = Match(Token_type.Comma, indexPointer)
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, out1["index"])
        Children.append(out2["node"])

        out3 = FunctionArgumentDash(out2["index"])
        if out3:
            out2 = out3
            Children.append(out3["node"])


        Node = Tree("FunctionArgumentDash", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return
