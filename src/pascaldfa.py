from automata.fa.dfa import DFA
"""
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
1- program 
2- program name
3- semicolomn
"""
dfa = DFA(
    states={'start', '1', '2', '3' 'end', 'error'},
    input_symbols={'Program', 'Identifier', 'Semicolon', 'AND', 'ARRAY'},
    transitions={
        'start': {'Program': '1', 'Identifier': 'error', 'Semicolon': 'error', 'AND': 'error', 'ARRAY': 'error'},
        '1': {'Program': 'error', 'Identifier': '2', 'Semicolon': 'error', 'AND': 'error', 'ARRAY': 'error'},
        '2': {'Program': 'error', 'Identifier': 'error', 'Semicolon': '3', 'AND': 'error', 'ARRAY': 'error'},
        '3': {'Program': 'error', 'Identifier': 'error', 'Semicolon': 'error', 'AND': 'error', 'ARRAY': 'error'},

        'end': {'Program': 'error', 'Identifier': 'error', 'Semicolon': 'error', 'AND': '1', 'ARRAY': 'error'},
        'error': {'Program': 'error', 'Identifier': 'error', 'Semicolon': 'error', 'AND': 'error', 'ARRAY': 'error'}

    },
    initial_state='start',
    final_states={'1', 'error'}
)
token = ['PROGRAM', 'AND']
steps = dfa.read_input_stepwise(token)
for i in steps:
    print(i)
