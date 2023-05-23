from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *
from PyQt6.QtCore import *
from compilers import *
import random
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

        self.testButton = self.findChild(QPushButton, 'testbutton')
        self.testButton.clicked.connect(self.randomgenerate)

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
        j = 0
        for i in Error:
            item1 = QStandardItem(str(i))
            self.errormodel.setItem(j, 0, item1)
            j += 1

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

    def randomgenerate(self):
        self.testclear()
        testcase =[
            """program FunctionExample;
var
num, square: Integer;
function CalculateSquare(num: Integer): Integer;
begin
CalculateSquare := num * num;
end;
begin
square := CalculateSquare(num);
end.""", """program LoopFunction;
function SumOfNumbers(n: integer): integer;

begin
var
    i, sum: integer;
    sum := n;
    for i := 1 to n do
        sum := sum + i;
    SumOfNumbers := sum;
end;
begin
end.""", """program FibonacciProgram;
function Fibonacci(n: integer): integer;
begin
    var i, a, b, c: integer;
    a := 0;
    b := 1;
    for i := 1 to 10 do
        Begin
        c := a + b;
        a := b;
        b := c;
        end;
        Fibonacci:=a;
end;
begin
end.""", """program MaxProgram;
function max(a: Integer; b: Integer): Integer;
var
  result: Integer;
begin
  if a > b then
    result := a;
  else
    result := b;
end;
begin
end.""", """program RepeatUntilFunctionExample;

var
  limit: Integer;
  result: Integer;

function CountUpToLimit(limit: Integer): Integer;
begin
  count := 1;

  repeat
    writeln("Count: ", count);
    count := count + 1;
  until count > limit;

  CountUpToLimit := count - 1;
end;

begin
  writeln("Enter a limit:");
  readln(limit);

  result := count - 1; 

  writeln("Loop finished!");
  writeln("Result: ", result);
end.""",
                    """program ProcedureExample;

uses
  crt;


procedure GreetUser;
var
  name: string;
begin
  writeln("Enter your name: ");
  readln(name);
  writeln("Hello, ", name, "! Welcome to the program.");
end;

procedure CalculateSum;
var
  num1, num2, sum: integer;
begin
  writeln("Enter the first number: ");
  readln(num1);
  writeln("Enter the second number: ");
  readln(num2);

  sum := num1 + num2;
  writeln("The sum of ", num1, " and ", num2, " is ", sum);
end;


begin
  for i := 1 to 10 do
        c := a + b;
        a := b;
        b := c;
end.""", """program RepeatUntilFunctionExample;

var
  limit: Integer;
  result: Integer;

function CountUpToLimit: Integer;
begin
  count := 1;

  repeat
    writeln("Count: ", count);
    count := count + 1;
  until count > limit;

  CountUpToLimit := count - 1;
end;

function CountUpToLimit2( 4gesg : INTEGER);
begin
  count2 := 1;

  repeat
    writeln("Count2: ", count2);
    count2 := count2 + 1;
  until count2 > limit2;

  CountUpToLimit2 := count2 - 1;
end;

function CountUpToLimit3;
begin
  count3 := 1;

  repeat
    writeln("Count3: ", count3);
    count3 := count3 + 1;
  until count3 > limit3;

  CountUpToLimit3 := count3 - 1;
end;

begin
  writeln("Enter a limit:");
  readln(limit);

  result := count - 1; 

  writeln("Loop finished!");
  writeln("Result: ", result);
end.""", """program Test;
begin
   writeln("Hello");
   writeln("World");
end.
""", """program Test;

var
   x, y, z: integer;

function Multiply(a: integer; b: integer): integer;
begin
   Multiply := a * b;
end;

procedure PrintResult(result: integer);
begin
   writeln("The result is: ", result);
end;

begin
   x := 5;
   y := 3;

   z := Multiply(x, y);

   PrintResult(z);
end.""", """program Factorial;
var
  i: integer;
  factorial: int;
function CalculateFactorial(number: integer): int;
begin
  factorial := 1;
  for i := 1 to number do
    factorial := factorial * i;
  CalculateFactorial := factorial;
end;

begin
  factorial := CalculateFactorial(number);
  writeln("The factorial of  is ", factorial);
end.""", """program TestGrammar;

uses
  SysUtils;

const
  MaxValue = 100.3213;

var
  x, y, z: integer;

function Multiply(a: integer; b: real): integer;
var
  result: integer;
begin
  result := a * b;
  Multiply := result;
end;

procedure PrintMessage(message: string);
begin
  writeln(message);
end;

procedure MyProcedure;
var
  a, b: integer;
begin
  a := 10;
  b := 20;
  writeln(a , b);
end;

begin
  writeln("Testing Pascal Grammar");

  x := 5;
  y := 3;

  if x > 0 then
    writeln("x is positive");

  for x := 1 to 10 do
  begin
    writeln(x);
  end;

  repeat
    x := x + 1;
    writeln(x);
  until x > 10;

  readln(x);

  write("The value of x is: ", x);

  writeln("Hello, world!");

  z := x + y * x - y;

  MyProcedure;

  z := Multiply(x, y);
  writeln("The result is: ", z);

  writeln("Program execution completed.");
end."""
]
        randomnumber=random.randrange(0,11)
        self.inputText.insertPlainText(testcase[randomnumber])


def main():
    app = QApplication([])
    home = Home()
    home.show()
    app.exec()


if __name__ == '__main__':
    main()
