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
from functions import *
from statementsFile import *
from statementsBody import *
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

    out2 = varDecleration(tempIndex)

    if out2:
        tempIndex = out2["index"]
        Children.append(out2["node"])
        

    out3 = FunctionDelaration(tempIndex)

    if out3:
        tempIndex = out3["index"]
        Children.append(out3["node"])

    out4 = procedureDecleration(tempIndex)

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
    return Tokens,errors
    
    #Token:Type List (have all token from the tokenizer)  , errors:Type List (Hold all the errors if there is one) 

def ShowTree_Qt6(Input):
    Tokens.clear()
    errors.clear()
    find_token(Input)
    Node = Parse()
    Node.draw()
    

def Scan():
    x1 = entry1.get()
    Tokens.clear()
    errors.clear()
    find_token(x1)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])

    # to display token stream as table
    dTDa1 = tk.Toplevel()
    dTDa1.title('Token Stream')
    dTDaPT = pt.Table(dTDa1, dataframe=df,
                      showtoolbar=True, showstatusbar=True)
    dTDaPT.show()
    # start Parsing
    Node = Parse()

    # to display errorlist
    if errors:
        df1 = pandas.DataFrame(errors)
        dTDa2 = tk.Toplevel()
        dTDa2.title('Error List')
        dTDaPT2 = pt.Table(dTDa2, dataframe=df1,
                           showtoolbar=True, showstatusbar=True)
        dTDaPT2.show()
    Node=str(Node)
    #Node=Node.replace('(statements )'," ")
    #Node=Node.replace("(procedureDecleration )"," ")
    #Node=Node.replace("(functionDecleration )"," ")
    #Node=Node.replace("(Decleration )"," ")
    print(Node)
    Node=Tree.fromstring(Node)
    
    Node.draw()

# GUI
if __name__ == "__main__":

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
    button1 = tk.Button(text='Scan', command=Scan, bg='brown',
                        fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)
    root.mainloop()
