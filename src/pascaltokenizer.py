from pascaltokens import *
import re


def find_token(text):
    arr = seperator(text)

    tokenizer(arr)


def seperator(text):
    splitters = [',', ':', ' ', '\n', ';', '+', '-',
                 '/', '*', '<', '>', '=', '(', ')']
    doublesplitters = [':=', '<=', '>=']
    SplittedArray = []
    tempArray = []
    counter = len(text)
    i = 0
    while (i < counter):
        if text[i] == '"':
            if tempArray:
                SplittedArray.append("".join(tempArray).strip())
                tempArray = []
            tempArray.append(text[i])
            i += 1
            while text[i] != '"' and i < counter:
                tempArray.append(text[i])
                i += 1
            tempArray.append(text[i])
            SplittedArray.append("".join(tempArray).strip())
            tempArray = []
        elif text[i] in splitters:
            if text[i:i+2] in doublesplitters:
                SplittedArray.append("".join(text[i:i+2]))
                i += 1
            else:
                if tempArray:
                    SplittedArray.append("".join(tempArray))
                if text[i] != ' ' and text[i] != '\n':
                    SplittedArray.append(text[i])
                elif text[i] == ' ' or text[i] == '\n':
                    while (text[i+1] == ' ' or text[i] == '\n'):
                        i += 1
            tempArray = []
        else:
            tempArray.append(text[i])
        i += 1
    if tempArray:
        SplittedArray.append("".join(tempArray).strip())

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
            ap = token(x, Token_type.Integer)
            Tokens.append(ap)
        elif re.match("^[a-zA-Z]$", x):
            ap = token(x, Token_type.Char)
            Tokens.append(ap)
        elif re.match("^[TRUE | FALSE]$", x):
            ap = token(x, Token_type.Boolean)
            Tokens.append(ap)
        elif re.match('^"[A-Za-z]*[0-9]*"$', x):
            ap = token(x, Token_type.Str)
            Tokens.append(ap)
        else:
            ap = token(x, Token_type.Error)
            Tokens.append(ap)
