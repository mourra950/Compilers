from enum import Enum
from nltk.tree import *
Tokens = []  # to add tokens to list
errors = []  # to add errors


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
    Error = 62
    Read = 63
    ReadLn = 64
    Write = 65
    WriteLn = 66
    IntegerType = 67
    Int = 68
    RealType = 69
    CharType = 70
    StringType = 71
    BooleanType = 72
    EndProgram = 73


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
    ";": Token_type.Semicolon,
    ",": Token_type.Comma,
    ":": Token_type.Colon,
    ":=": Token_type.Assignment,
    "USES": Token_type.Uses,
    "READ": Token_type.Read,
    "READLN": Token_type.ReadLn,
    "WRITE": Token_type.Write,
    "WRITELN": Token_type.WriteLn,
    "INTEGER": Token_type.IntegerType,
    "REAL": Token_type.RealType,
    "CHAR": Token_type.CharType,
    "STRING": Token_type.StringType,
    "BOOLEAN": Token_type.BooleanType,
    "END.": Token_type.EndProgram,

    # "IDENTIFIER": Token_type.Identifier,
    # "CONSTANT" : Token_type.Constant,
    # "REAL" : Token_type.Real,
    # "CHAR" : Token_type.Char,
    # "BOOLEAN" : Token_type.Boolean,


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
