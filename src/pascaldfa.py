from automata.fa.dfa import DFA
from transitiondfa import transitionsdfa
from visual_automata.fa.dfa import VisualDFA
"""
start
A
"AND" 2 ,3 
"ARRAY" 4,5,6,7
B
"BEGIN" 8,9,10,11
"BOOLEAN" 12,13,14,15,16,17
C
"CASE" 18,19,20
"CHAR" 21,22,23
"CONST" 24,25,26,27
D
"DIV" 29 , 30 
DO
"DO"  
"DOWNTO" 31,32,33,34
E
"ELSE" 35,36,37
"END" 38,39
F
"FILE" 40,41,42
"FOR" 43,44
"FUNCTION" 45,46,47,48,49,50,51
G
"GOTO" 52,53,54
I
"IF" 55
IN
"IN" 
"INTEGER" 56,57,58,59,60
L
"LABEL" 61,62,63,64
M
"MODE" 65,66,67
N
"NIL" 68,69
"NOT" 70,71
O
"OF" 72
"OR" 73
P
"PACKED" 74,75,76,77,78
PR
PRO
"PROCEDURE" 79, 80, 81, 82, 83, 84
"PROGRAM" 85, 86, 87, 88, 89
R
RE

"RECORD" 90 91 92 93 
"REPEAT" 94 95 96 97
REA
"REAL"  98
READ
"READ"
"READLN" 99 100
S
"SET" 101 102
"STRING" 103 104 105 106 107 
T
"THEN" 108 109 110 
"TO" 111
"TYPE" 112 113 114 
U
"UNTIL" 115 116 117 118 
"USES" 119 120 121 

"VAR" 122 123 124
W
"WHILE" 125 126 127 128
"WITH" 129 130 131
WR
WRI
WRIT
WRITE
"WRITE" 
"WRITELN" 132 133
"("
")"
{
"{"
"{*" 134
"}"   
*
"*"
"*}" 135
"<"   
"<="
">"
">="
"="
"+"
"-"
"/"













'And', 'Array', 'Begin', 'Case', 'Const',
'Div', 'DownTo', 'Else', 'End', 'File', 'For',
'Function', 'GoTo', 'If', 'In', 'Label', 'Mode',
'Nil', 'Not', 'Of', 'Or', 'Packed', 'Procedure', 'Program',
'Record', 'Repeat', 'Set', 'Then', 'To', 'Type', 'Until', 'Var',
'While', 'With', 'Do', 'PlusOp', 'MinusOp', 'MultiplyOp', 'DivideOp',
'LessEqual', 'GreatEqual', 'Equal', 'Greater', 'Lesser',
'OpenMultiComment', 'CloseMultiComment', 'OpenComment', 'CloseComment',
'OpenGroup', 'CloseGroup', 'Semicolon', 'Colon', 'Assignment', 'Str', 'Identifier',
'Uses', 'Comma', 'Constant', 'Real', 'Char', 'Boolean', 'Error',
'Read', 'ReadLn', 'Write', 'WriteLn', 'Integer', 'Int', 'RealType',
'CharType', 'StringType', 'BooleanType'
"""
"""
program declaration
--------------------------
1- program 
2- Identifier
3- semicolomn
----------------------------

function declaration
---------------------------------------
4-function
5-Identifier
++++++++++++++++++++++++++++++++++++++++
6- semicolomn
++++++++++++++++++++++++++++++++++++++++
7-OpenGroup
8-Identifier
9-Colon
10-Integertype|RealType|CharType|StringType|BooleanType
11-CloseGroup
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++



++++++++++++++++++++++++++++++++++++++++

5-OpenGroup
6-Colon
7-Int
8-Real
9-Char
10-Boolean
11-Str
12-Integertype
13-RealType
14-CharType
15-StringType
16-BooleanType
17-CloseGroup
"""
# for i in transitionsdfa:
#     print(i)
dfa = DFA(
    states={'Start', 'IDENTIFIER',
            'A',
            'AN', 'AND',
            'AR', 'ARR', 'ARRA', 'ARRAY',
            'B', 'BE', 'BEG', 'BEGI', 'BEGIN',
            'BO', 'BOO', 'BOOL', 'BOOLE', 'BOOLEA', 'BOOLEAN',
            'C', 'CA', 'CAS', 'CASE',
            'CH', 'CHA', 'CHAR',
            'CO', 'CON', 'CONS', 'CONST',
            'D', 'DI', 'DIV',
            'DO',
            'DOW', 'DOWN',
            'DOWNT', 'DOWNTO',
            'E', 'EL', 'ELS', 'ELSE',
            'EN', 'END',
            'F', 'FI', 'FIL', 'FILE',
            'FO', 'FOR',
            'FU', 'FUN', 'FUNC', 'FUNCT', 'FUNCTI', 'FUNCTIO', 'FUNCTION',
            'G', 'GO', 'GOT', 'GOTO',
            'I', 'IF',
            'IN',
            'INT', 'INTE', 'INTEG', 'INTEGE', 'INTEGER',
            'L', 'LA', 'LAB', 'LABE', 'LABEL',
            'M', 'MO', 'MOD', 'MODE',
            'N', 'NI', 'NIL',
            'NO', 'NOT',
            'O', 'OF',
            'OR',
            'P', 'PA', 'PAC', 'PACK', 'PACKE', 'PACKED',
            'PR', 'PRO', 'PROC', 'PROCE', 'PROCED', 'PROCEDU', 'PROCEDUR', 'PROCEDURE',
            'PROG', 'PROGR', 'PROGRA', 'PROGRAM',
            'R', 'RE', 'REC', 'RECO', 'RECOR', 'RECORD',
            'REP', 'REPE', 'REPEA', 'REPEAT',
            'REA', 'REAL',
            'READ',
            'READL', 'READLN',
            'S', 'SE', 'SET',
            'ST', 'STR', 'STRI', 'STRIN', 'STRING',
            'T', 'TH', 'THE', 'THEN',
            'TO',
            'TY', 'TYP', 'TYPE',
            'U', 'UN', 'UNT', 'UNTI', 'UNTIL',
            'US', 'USE', 'USES',
            'V', 'VA', 'VAR',
            'W', 'WH', 'WHI', 'WHIL', 'WHILE',
            'WR', 'WRI', 'WRIT', 'WRITE',
            'WRITEL', 'WRITELN',
            'INTEGERstate', 'REAL', 'ERROR', '(',
            ')', '{', '}', '<', '>', '=', '+', '-', '*', '/',
            '<=', '>='},
    input_symbols={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   '(', ')', '{', '}', '<', '>', '=', '+', '-', '*', '/',
                   },
    transitions=transitionsdfa,
    initial_state='Start',
    final_states={'Start', 'IDENTIFIER', 'A', 'AN', 'AND', 'AR', 'ARR', 'ARRA', 'ARRAY', 'B', 'BE', 'BEG', 'BEGI', 'BEGIN',
                  'BO', 'BOO', 'BOOL', 'BOOLE', 'BOOLEA', 'BOOLEAN', 'C', 'CA', 'CAS', 'CASE', 'CH', 'CHA', 'CHAR', 'CO', 'CON', 'CONS', 'CONST',
                  'D', 'DI', 'DIV', 'DO', 'DOW', 'DOWN', 'DOWNT', 'DOWNTO', 'E', 'EL', 'ELS', 'ELSE', 'EN', 'END', 'F', 'FI', 'FIL', 'FILE', 'FO', 'FOR',
                  'FU', 'FUN', 'FUNC', 'FUNCT', 'FUNCTI', 'FUNCTIO', 'FUNCTION', 'G', 'GO', 'GOT', 'GOTO', 'I', 'IF', 'IN', 'INT', 'INTE', 'INTEG',
                  'INTEGE', 'INTEGER', 'L', 'LA', 'LAB', 'LABE', 'LABEL', 'M', 'MO', 'MOD', 'MODE', 'N', 'NI', 'NIL', 'NO', 'NOT', 'O', 'OF', 'OR', 'P', 'PA', 'PAC', 'PACK',
                  'PACKED', 'PR', 'PRO', 'PROC', 'PROCE', 'PROCED', 'PROCEDU', 'PROCEDUR', 'PROCEDURE', 'PROG', 'PROGR', 'PROGRA', 'PROGRAM', 'R', 'RE', 'REC',
                  'RECO', 'RECOR', 'RECORD', 'REP', 'REPE', 'REPEA', 'REPEAT', 'REA', 'REAL', 'READ', 'READL', 'READLN', 'S', 'SE', 'SET', 'ST', 'STR', 'STRI', 'STRIN',
                  'STRING', 'T', 'TH', 'THE', 'THEN', 'TO', 'TY', 'TYP', 'TYPE', 'U', 'UN', 'UNT', 'UNTI', 'UNTIL', 'US', 'USE', 'USES', 'V', 'VA', 'VAR', 'W', 'WH', 'WHI',
                  'WHIL', 'WHILE', 'WR', 'WRI', 'WRIT', 'WRITE', 'WRITEL', 'WRITELN', 'INTEGERstate', 'REAL',
                  '(', ')', '{', '}', '<', '>', '=', '+', '-', '*', '/',
                  }
)
token = '21OSAODOASD'
steps = dfa.read_input_stepwise(token)
try:
    for i in steps:
        print(i)
except:
    pass
# dfar = VisualDFA(dfa)
# dfar.show_diagram(filename='DFAA',view=True,state_seperation=4)
dfa.show_diagram()
# print(dfar.table)
# print('ahmed')
