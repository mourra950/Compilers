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
from functionDecleration import *


def Parse():
    j = 0
    Children = []
    Header_dict = Header(j)
    Children.append(Header_dict["node"])
    Decleration_dict = Decleration(Header_dict["index"])
    Children.append(Decleration_dict["node"])
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
    programDict = ProgramName(indexPointer)
    Children.append(programDict["node"])

    tempDict = Match(Token_type.Uses, programDict["index"])


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
    out1 = Match(Token_type.Identifier, indexPointer, True)

    if re.match("^[a-zA-Z][a-zA-Z0-9]*$", str(out1["node"])):
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

        Node = Tree("ConstNameDash", Children)
        output["node"] = Node
        output["index"] = out4["index"]
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
        if errors:
            errors.pop()
        return






def Decleration(indexPointer):
    Children = []
    output = dict()

    out1 = constDeleration(indexPointer)
    

    outTemp = {}
    tempIndex = indexPointer
    if out1:
        tempIndex = out1["index"]
        Children.append(out1["node"])

    out2 = varDecleration(tempIndex)

    if out2:
        tempIndex = out2["index"]
        Children.append(out2["node"])
           
    # out3 = functionDecleration(tempIndex)

    # if out3:
    #     tempIndex = out3["index"]

    # out4 = procedureDecleration(tempIndex)



    # if out1:
    #     outTemp = out1
    #     Children.append(out1["node"])
    #     out2 = varDecleration(out1["index"])
    #     if out2:
    #         outTemp = out2
    #         Children.append(out2["node"])
    #         out3 = functionDecleration(out2["index"])
    #         if out3:
    #             outTemp = out3
    #             Children.append(out3["node"])
    #             out4 = procedureDecleration(out3["index"])
    #             if out4:
    #                 outTemp = out4
    #                 Children.append(out4["node"])
    # else:

    #     out2 = varDecleration(indexPointer)
    # if out2:
    #     outTemp = out2
    #     Children.append(out2["node"])
    
    

    
    Node = Tree("Decleration", Children)
    output["node"] = Node
    # if outTemp:
    #     output["index"] = outTemp["index"]
    # else:
    output["index"] = tempIndex
    return output


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
    Node.draw()
    # clear your list
    # label3 = tk.Label(root, text='Lexem ' + x1 + ' is:', font=('helvetica', 10))
    # canvas1.create_window(200, 210, window=label3)

    # label4 = tk.Label(root, text="Token_type"+x1, font=('helvetica', 10, 'bold'))
    # canvas1.create_window(200, 230, window=label4)


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
button1 = tk.Button(text='Scan', command=Scan, bg='brown',
                    fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()
