import tkinter as tk
from enum import Enum
import re
import pandas
import pandastable as pt
from nltk.tree import *


class Token_type(Enum):
    And = 1
    Array = 2
    Begin = 3
    Case = 4
    Const = 5
    Div = 6
    DownTo = 7
    Else = 8
    End = 9
    File = 10
    For = 11
    Function = 12
    GoTo = 13
    If = 14
    In = 15
    Label = 16
    Mode = 17
    Nil = 18
    Not = 19
    Of = 20
    Or = 21
    Packed = 22
    Procedure = 23
    Program = 24
    Record = 25
    Repeat = 26
    Set = 27
    Then = 28
    To = 29
    Type = 30
    Until = 31
    Var = 32
    While = 33
    With = 34
    Do = 35
    PlusOp = 36
    MinusOp = 37
    MultiplyOp = 38
    DivideOp = 39
    LessEqual = 40
    GreatEqual = 41
    Equal = 42
    Greater = 43
    Lesser = 44
    OpenMultiComment = 45
    CloseMultiComment = 46
    OpenComment = 47
    CloseComment = 48
    OpenGroup = 49
    CloseGroup = 50
    Semicolon = 51
    Colon = 52
    Assignment = 53
    Str = 54
    Identifier = 55
    Uses = 56
    Comma = 57
    Constant = 58
    Real = 59
    Char = 60
    Boolean = 61


class token:
    def __init__(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type

    def to_dict(self):
        return {
            'Lex': self.lex,
            'token_type': self.token_type
        }


# Reserved word Dictionary
ReservedWords = {                       # We Can add global?
    "AND": Token_type.And,
    "ARRAY": Token_type.Array,
    "BEGIN": Token_type.Begin,
    "CASE": Token_type.Case,
    "CONST": Token_type.Const,
    "DIV": Token_type.Div,
    "DOWNTO": Token_type.DownTo,
    "ELSE": Token_type.Else,
    "END": Token_type.End,
    "FILE": Token_type.File,
    "FOR": Token_type.For,
    "FUNCTION": Token_type.Function,
    "GOTO": Token_type.GoTo,
    "IF": Token_type.If,
    "IN": Token_type.In,
    "LABEL": Token_type.Label,
    "MODE": Token_type.Mode,
    "NIL": Token_type.Nil,
    "NOT": Token_type.Not,
    "OF": Token_type.Of,
    "OR": Token_type.Or,
    "PACKED": Token_type.Packed,
    "PROCEDURE": Token_type.Procedure,
    "PROGRAM": Token_type.Program,
    "RECORD": Token_type.Record,
    "REPEAT": Token_type.Repeat,
    "SET": Token_type.Set,
    "THEN": Token_type.Then,
    "TO": Token_type.To,
    "TYPE": Token_type.Type,
    "UNTIL": Token_type.Until,
    "VAR": Token_type.Var,
    "STR": Token_type.Str,
    "WHILE": Token_type.While,
    "WITH": Token_type.With,
    "DO": Token_type.Do,
    ";": Token_type.Semicolon,
    ",": Token_type.Comma,
    ":": Token_type.Colon,
    ":=": Token_type.Assignment,
    "USES": Token_type.Uses,

}
Operators = {
    "+": Token_type.PlusOp,
    "-": Token_type.MinusOp,
    "*": Token_type.MultiplyOp,
    "/": Token_type.DivideOp
}
RelationOperators = {
    "<=": Token_type.LessEqual,
    ">=": Token_type.GreatEqual,
    "=": Token_type.Equal,
    ">": Token_type.Greater,
    "<": Token_type.Lesser
}
Comment = {
    "{*": Token_type.OpenMultiComment,
    "*}": Token_type.CloseMultiComment,
    "{": Token_type.OpenComment,
    "}": Token_type.CloseComment,
}
Group = {
    "(": Token_type.OpenGroup,
    ")": Token_type.CloseGroup,
}
Tokens = []  # to add tokens to list
errors = []


def find_token(text):
    arr = seperator(text)
    # print(arr)
    tokenizer(arr)


def seperator(text):
    splitters = [',', ':', ' ', ';', '+', '-', '/', '*', '<', '>', '=']
    doublesplitters = [':=', '<=', '>=']
    SplittedArray = []
    tempArray = []
    counter = len(text)
    i = 0
    while (i < counter):
        # print(text[i])
        if text[i] in splitters:
            if text[i:i+2] in doublesplitters:
                SplittedArray.append("".join(text[i:i+2]))
                i += 1
            else:
                if tempArray:
                    SplittedArray.append("".join(tempArray))
                if text[i] != ' ':
                    SplittedArray.append(text[i])
                elif text[i] == ' ':
                    while (text[i+1] == ' '):
                        i += 1
            tempArray = []
        else:
            tempArray.append(text[i])
        i += 1
    if tempArray:
        SplittedArray.append("".join(tempArray))

    return SplittedArray


def tokenizer(T):
    # Tokens = []  # to add tokens to list
    for x in T:
        x = x.upper()
        if x in ReservedWords:
            ap = token(x, ReservedWords[x])
            Tokens.append(ap)
        elif x in Operators:
            ap = token(x, Operators[x])
            Tokens.append(ap)
        elif x in RelationOperators:
            ap = token(x, RelationOperators[x])
            Tokens.append(ap)
        elif x in Group:
            ap = token(x, Group[x])
            Tokens.append(ap)
        elif x in Comment:
            ap = token(x, Comment[x])
            Tokens.append(ap)
        elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", x):
            ap = token(x, Token_type.Identifier)
            Tokens.append(ap)
        elif re.match("^[0-9].[0-9]$", x):
            ap = token(x, Token_type.Real)
            Tokens.append(ap)
        elif re.match("^[0-9]*$", x):
            ap = token(x, Token_type.Constant)
            Tokens.append(ap)
        else:
            ap = token(x, Token_type.Error)
            Tokens.append(ap)
            


def Parse():
    j = 0
    Children = []
    Header_dict = Header(j)

    if Header_dict:
        Children.append(Header_dict["node"])

        Decleration_dict = Decleration(Header_dict["index"])   
        Children.append(Decleration_dict["node"])
#     Block_dict = Block(Header_dict["index"])
#     Children.append(block_dict["node"])
    # dic_output = Match(Token_type.Dot, j)
    # Children.append(dic_output["node"])
    Node = Tree('Program', Children)

    return Node


def ProgramName(indexPointer):
    Children = []
    output = dict()

    out1 = Match(Token_type.Program, indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Identifier, out1["index"])
    Children.append(out2["node"])

    out3 = Match(Token_type.Semicolon, out2["index"])
    Children.append(out3["node"])

    Node = Tree("ProgramName", Children)
    output["node"] = Node
    output["index"] = out3["index"]
    return output


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
    print(out2, 'library ')
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
        print(out1["node"], 'library dash')
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
        return


def Header(indexPointer):
    Children = []
    output = dict()
    programDict = ProgramName(indexPointer)
    Children.append(programDict["node"])
    
    tempDict = Match(Token_type.Uses, programDict["index"])
    print(str(tempDict['node']))
    
   
    if (str(tempDict["node"]) == 'USES'):
        programDict = LibrarySection(programDict["index"])
        Children.append(programDict["node"])

    Node = Tree("Header", Children)
    output["node"] = Node
    output["index"] = programDict["index"]
    return output


def ConstNameDash(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Identifier, indexPointer)
    if str(out1["node"]) == 'IDENTIFIER':
        Children.append(out1["node"])

        out2 = Match(Token_type.Equal, indexPointer)
        Children.append(out2["node"])

        out3 = Match(Token_type.Constant, out2["index"])
        Children.append(out3["node"])

        out4 = Match(Token_type.Semicolon, out3["index"])
        Children.append(out4["node"])

        out5 = ConstNameDash(out4["index"])
        Children.append(out5["node"])

        Node = Tree("ConstNameDash", Children)
        output["node"] = Node
        output["index"] = out5["index"]
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


def constDeleration(indexPointer):
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
        return


def DataType(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Constant, indexPointer)
    out2 = Match(Token_type.Real, indexPointer)
    out3 = Match(Token_type.Char, indexPointer)
    out4 = Match(Token_type.Identifier, indexPointer)
    out5 = Match(Token_type.Boolean, indexPointer)
    Node = Tree("DataType", Children)
    if str(out1["node"]) == 'CONSTANT':
        Children.append(out1["node"])
        output["node"] = Node
        output["index"] = out1["index"]

    elif str(out2["node"]) == 'REAL':
        Children.append(out2["node"])
        output["node"] = Node
        output["index"] = out2["index"]

    elif str(out3["node"]) == 'CHAR':
        Children.append(out3["node"])
        output["node"] = Node
        output["index"] = out3["index"]

    elif str(out4["node"]) == 'IDENTIFIER':
        Children.append(out4["node"])
        output["node"] = Node
        output["index"] = out4["index"]

    elif str(out5["node"]) == 'BOOLEAN':
        Children.append(out5["node"])
        output["node"] = Node
        output["index"] = out5["index"]
    return output


def VarNameDash(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Comma, indexPointer)
    if str(out1["node"]) == ',':
        Children.append(out1["node"])

        out2 = Match(Token_type.Identifier, indexPointer)
        Children.append(out2["node"])

        out3 = VarNameDash(indexPointer)
        Children.append(out3["node"])

        Node = Tree("VarNameDash", Children)
        output["node"] = Node
        output["index"] = out3["index"]
        return output
    else:
        return


def VarName(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Identifier, indexPointer)
    Children.append(out1["node"])

    out2 = VarNameDash(indexPointer)
    Children.append(out2["node"])

    Node = Tree("VarName", Children)
    output["node"] = Node
    output["index"] = out2["index"]
    return output


def varDecleration1Dash(indexPointer):              # CHECK CODE AGAIN
    Children = []
    output = dict()
    out1 = VarName(indexPointer)
    if str(out1["node"]) == 'IDENTIFIER':
        Children.append(out1["node"])

        out2 = Match(Token_type.Colon, indexPointer)
        Children.append(out2["node"])

        out3 = DataType(out2["index"])
        Children.append(out3["node"])

        out4 = Match(Token_type.Semicolon, out3["index"])
        Children.append(out4["node"])

        out5 = varDecleration1Dash(out4["index"])
        Children.append(out5["node"])

        Node = Tree("varDecleration1Dash", Children)
        output["node"] = Node
        output["index"] = out5["index"]
        return output
    else:
        return


def varDecleration1(indexPointer):
    Children = []
    output = dict()
    out1 = VarName(indexPointer)
    Children.append(out1["node"])

    out2 = Match(Token_type.Colon, indexPointer)
    Children.append(out2["node"])

    out3 = DataType(out2["index"])
    Children.append(out3["node"])

    out4 = Match(Token_type.Semicolon, out3["index"])
    Children.append(out4["node"])

    out5 = varDecleration1Dash(out4["index"])
    Children.append(out5["node"])

    Node = Tree("varDecleration1", Children)
    output["node"] = Node
    output["index"] = out5["index"]
    return output


def varDecleration(indexPointer):
    Children = []
    output = dict()
    out1 = Match(Token_type.Var, indexPointer)
    if str(out1["node"]) == 'VAR':
        Children.append(out1["node"])

        out2 = varDecleration1(out1["index"])
        Children.append(out2["node"])

        Node = Tree("varDecleration", Children)
        output["node"] = Node
        output["index"] = out2["index"]
        return output
    else:
        return


def Decleration(indexPointer):
    Children = []
    output = dict()
    tempIndex = indexPointer

    out1 = constDeleration(indexPointer)
    if out1: 
        tempIndex = out1
        Children.append(out1["node"])

    out2 = varDecleration(tempIndex["index"])
    if out2:
        tempIndex = out2
        Children.append(out2["node"])

    # out3 = functionDeleration(out2["index"])
    # Children.append(out3["node"])

    # out4 = procedureDecleration(out3["index"])
    # Children.append(out4["node"])

    Node = Tree("Decleration", Children)
    output["node"] = Node
    output["index"] = tempIndex["index"]
    return output


def Match(a, j):
    output = dict()
    if (j < len(Tokens)):
        Temp = Tokens[j].to_dict()
        if (Temp['token_type'] == a):
            j += 1
            output["node"] = Temp['Lex']
            output["index"] = j
            return output
        else:
            output["node"] = ["error"]
            output["index"] = j+1
            errors.append("Syntax error : ")
            return output
    else:
        output["node"] = ["error"]
        output["index"] = j+1
        return output


# GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Scanner Phase')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Source code:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def Scan():
    x1 = entry1.get()
    find_token(x1)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    # print(df)

    # to display token stream as table
    dTDa1 = tk.Toplevel()
    dTDa1.title('Token Stream')
    dTDaPT = pt.Table(dTDa1, dataframe=df,
                      showtoolbar=True, showstatusbar=True)
    dTDaPT.show()
    # start Parsing
    Node = Parse()

    # to display errorlist
    df1 = pandas.DataFrame(errors)
    dTDa2 = tk.Toplevel()
    dTDa2.title('Error List')
    dTDaPT2 = pt.Table(dTDa2, dataframe=df1,
                       showtoolbar=True, showstatusbar=True)
    dTDaPT2.show()
    Node.draw()
    # clear your list

    # label3 = tk.Label(root, text='Lexem ' + x1 + ' is:', font=('helvetica', 10))
    # canvas1.create_window(200, 210, window=label3)

    # label4 = tk.Label(root, text="Token_type"+x1, font=('helvetica', 10, 'bold'))
    # canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Scan', command=Scan, bg='brown',
                    fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()
