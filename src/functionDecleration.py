# from utils import *

# def functionDecleration(indexPointer):
#     Children = []
#     output = dict()

#     out1 = Match(Token_type.Function, indexPointer, True)
#     if out1:
#         Children.append(out1["node"])

#         out2 = Match(Token_type.Identifier, out1["index"])
#         Children.append(out2["node"])

#         out3 = arguments(ou2["index"])

        
    
#     else:
#         functionDeclerationDash(indexPointer)


#     Node = Tree("Header", Children)
#     output["node"] = Node
#     output["index"] = programDict["index"]
#     return output