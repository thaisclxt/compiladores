from classes.state import State
from classes.automaton import Automaton


def recursion(state: State, automaton: Automaton):
    output = f'{state.index}'
    for transition in automaton.transitions:
        if transition.from_state == state and transition.symbol == 'ε':
            output += f' {recursion(transition.to_state, automaton)}'

    return output


def fecho_algorithm(automaton: Automaton):
    for state in automaton.states:
        output = recursion(state, automaton).split(' ')
        output = [int(x) for x in output]
        output.sort()

        output = [f'q{x}' for x in output]
        print(line(state.index, output))


def line(index_from, output):
    return f'Fecho-ε(q{index_from}) = {{{", ".join(output)}}}'
