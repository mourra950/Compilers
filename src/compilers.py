import tkinter as tk
from enum import Enum
import re
import pandas
import pandastable as pt
from nltk.tree import *
from pascaltokens import *
from pascaltokenizer import *
from library import *
from var import *
from statementsFile import *
from constpascal import *
from procedures import *


def Parse():
    j = 0
    Children = []
    Header_dict = Header(j)
    Children.append(Header_dict["node"])
    tempNode = Header_dict
    Decleration_dict = Decleration(tempNode["index"])
    if Decleration_dict:
        tempNode = Decleration_dict
        Children.append(Decleration_dict["node"])

    Exec_dict = execution(tempNode["index"])
    Children.append(Exec_dict["node"])
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


def Header(indexPointer):
    Children = []
    output = dict()

    out1 = ProgramName(indexPointer)
    Children.append(out1["node"])

    out2 = LibrarySection(out1["index"])
    if out2:
        out1 = out2
        Children.append(out2["node"])

    Node = Tree("Header", Children)
    output["node"] = Node
    output["index"] = out1["index"]
    return output


def Decleration(indexPointer):
    Children = []
    output = dict()

    out1 = constDecleration(indexPointer)

    tempIndex = indexPointer
    if out1:
        tempIndex = out1["index"]
        Children.append(out1["node"])

    out2 = varDeclaration(tempIndex)

    if out2:
        tempIndex = out2["index"]
        Children.append(out2["node"])

    out3 = FunctionDeclaration(tempIndex)

    if out3:
        tempIndex = out3["index"]
        Children.append(out3["node"])

    out4 = procedureDeclaration(tempIndex)

    if out4:
        tempIndex = out4["index"]
        Children.append(out4["node"])

    if Children:
        Node = Tree("Decleration", Children)
        output["node"] = Node
        output["index"] = tempIndex
        return output
    else:
        return


def Scan_Qt6(Input):
    Tokens.clear()
    errors.clear()
    find_token(Input)
    Node = Parse()
    if error_comments:
        errors.append(error_comments)
    return Tokens, errors

    # Token:Type List (have all token from the tokenizer)  , errors:Type List (Hold all the errors if there is one)


def ShowTree_Qt6(Input):
    Tokens.clear()
    errors.clear()
    find_token(Input)
    Node = Parse()
    print(type(Node))

    Node = str(Node)
    Node = Node.replace('(statements )', " ")
    Node = Node.replace("(procedureDeclaration )", " ")
    Node = Node.replace("(FunctionDeclaration )", " ")
    Node = Node.replace("(Decleration )", " ")
    Node = Tree.fromstring(Node)

    Node.draw()


# GUI
if __name__ == "__main__":

    Node = """(= (Asd Awad-> As-> Awadawdawdad))"""
    
    Node = Tree.fromstring('(Node a b c)' )

    Node.draw()
