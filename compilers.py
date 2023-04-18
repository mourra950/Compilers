import tkinter as tk
from enum import Enum
import re
import pandas


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
    "WHILE": Token_type.While,
    "WITH": Token_type.With,
    "DO": Token_type.Do,

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


def find_token(text):
    T = text.split()
    for x in T:
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
            ap = token(x, Token_type.Va)
            Tokens.append(ap)
        elif re.match("^[0-9].[0-9]$",x):
            ap =token(x,Token_type.Constant)
            Tokens.append(ap)
        elif re.match("^[0-9]*$", x):
            ap = token(x, Token_type.Constant)
            Tokens.append(ap)
        else:
            ap = token(x, Token_type.Error)
            Tokens.append(ap)


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
    label3 = tk.Label(root, text='Lexem ' + x1 +
                      ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    x1 = str(df.token_type)

    label4 = tk.Label(root, text="Token_type"+x1,
                      font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Scan', command=Scan, bg='brown',
                    fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
