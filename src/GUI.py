from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *
from PyQt6.QtCore import *
from compilers import *

Lex = ['aashda', 'adasda', 'sadaw a', 'asdwda']
Token = ['Int', 'Int', 'Int', 'Int']


class Home(QMainWindow):
    def __init__(self) -> None:
        super(Home, self).__init__()
        loadUi('./Compiler_gui.ui', self)

        self.Viewtest1 = self.findChild(QTableView, 'tableView')
        
        self.compileButton = self.findChild(QPushButton, 'Compile_button')
        self.compileButton.clicked.connect(self.testPopulate)
        
        self.showParseTree = self.findChild(QPushButton, 'Show_ParseTree')
        self.showParseTree.clicked.connect(self.testshowTree)
        
        self.inputText = self.findChild(QTextEdit, 'Text_input')
      
        self.clearButton = self.findChild(QPushButton, 'Clear_button')
        self.clearButton.clicked.connect(self.testclear)
        
        self.model = QStandardItemModel()
        self.Viewtest1.setModel(self.model)
        self.set_table_headers(['Lex', 'Token Type'])
    def set_table_headers(self, headers):
        self.model.setHorizontalHeaderLabels(headers)
    def set_cell_data(self, row, column, data):
        item = QStandardItem(data)
        self.model.setItem(row, column, item)
    def populate_Table(self,Token):
        for i in range(len(Token)):
            item1 = QStandardItem(str(Token[i].lex))
            item2 = QStandardItem(str(Token[i].token_type))
            self.model.setItem(i, 0, item1)
            self.model.setItem(i, 1, item2)
    def testPopulate(self):
        Input=self.inputText.toPlainText()
        Tokens,errors=Scan_Qt6(Input)
        for i in Tokens:
            print(i.lex)
        self.populate_Table(Tokens)
        
        
    def testclear(self):
        self.model.clear()
        self.set_table_headers(['Lex', 'Token Type'])
        self.inputText.clear()
    
    def testshowTree(self):
        Input=self.inputText.toPlainText()
        ShowTree_Qt6(Input)


def main():
    app = QApplication([])
    home = Home()
    home.show()
    app.exec()

if __name__ == '__main__':
    main()
