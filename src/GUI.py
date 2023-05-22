from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *
from PyQt6.QtCore import *
from compilers import *


# TODO: Match Some Functions REDO, ERRORS HANDLING, Check all datatypes are correct by testing it
class Home(QMainWindow):
    def __init__(self) -> None:
        super(Home, self).__init__()
        loadUi('./Compiler_gui.ui', self)
        self.c = 0
        self.tokenviewtable = self.findChild(QTableView, 'tableView')
        self.errorviewtable = self.findChild(QTableView, 'tableviewerror')
        self.compileButton = self.findChild(QPushButton, 'Compile_button')
        self.compileButton.clicked.connect(self.testPopulate)
        self.showParseTree = self.findChild(QPushButton, 'Show_ParseTree')
        self.showParseTree.clicked.connect(self.testshowTree)
        self.inputText = self.findChild(QTextEdit, 'Text_input')
        self.clearButton = self.findChild(QPushButton, 'Clear_button')
        self.clearButton.clicked.connect(self.testclear)
        self.tokenmodel = QStandardItemModel()
        self.tokenviewtable.setModel(self.tokenmodel)
        self.set_table_headers(['Lex', 'Token Type'])
        self.errormodel = QStandardItemModel()
        self.errorviewtable.setModel(self.errormodel)
        self.set_table_errorheaders(['Error'])

    def set_table_headers(self, headers):
        self.tokenmodel.setHorizontalHeaderLabels(headers)

    def set_table_errorheaders(self, headers):
        self.errormodel.setHorizontalHeaderLabels(headers)

    def set_cell_data(self, row, column, data):
        item = QStandardItem(data)
        self.tokenmodel.setItem(row, column, item)

    def set_error_data(self, row, column, data):
        item = QStandardItem(data)
        self.errormodel.setItem(row, column, item)

    def populate_Table(self, Token):
        for i in range(len(Token)):
            item1 = QStandardItem(str(Token[i].lex))
            item2 = QStandardItem(str(Token[i].token_type))
            self.tokenmodel.setItem(i, 0, item1)
            self.tokenmodel.setItem(i, 1, item2)

    def populate_errorTable(self, Error):
        j =0
        for i in Error:
            item1 = QStandardItem(str(i))
            self.errormodel.setItem(j, 0, item1)
            j+=1

    def testPopulate(self):
        self.compileclear()
        Input = self.inputText.toPlainText()
        Tokens, Errors = Scan_Qt6(Input)
        self.populate_Table(Tokens)
        self.populate_errorTable(Errors)
       

    def testclear(self):
        self.tokenmodel.clear()
        self.set_table_headers(['Lex', 'Token Type'])
        self.inputText.clear()
        self.set_table_errorheaders(['Error Tokens'])
    def compileclear(self):
        self.tokenmodel.clear()
        self.errormodel.clear()
        self.set_table_headers(['Lex', 'Token Type'])
        self.set_table_errorheaders(['Errors'])
        

    def testshowTree(self):
        Input = self.inputText.toPlainText()
        ShowTree_Qt6(Input)


def main():
    app = QApplication([])
    home = Home()
    home.show()
    app.exec()


if __name__ == '__main__':
    main()
