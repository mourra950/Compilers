from automata.fa.dfa import DFA


dfa = DFA(
    states={'program', 'header', 'declaration',
            'execution','librarySection' ,'4', '5', '6', 'dead'},
    input_symbols={'+', '-', '/', '*', 'ID', 'NUM'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}},
    initial_state='q0',
    final_states={'q1'}
)
