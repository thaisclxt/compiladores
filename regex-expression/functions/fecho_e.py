from classes.state import State
from classes.automaton import Automaton


def recursion(state: State, automaton: Automaton):
    output = f'{state.index}'
    for transition in automaton.transitions:
        if transition.from_state == state and transition.symbol == 'ε':
            output += f', q{recursion(transition.to_state, automaton)}'

    return output


def fecho_algotithm(automaton: Automaton):
    for state in automaton.states:
        print(line(state.index, recursion(state, automaton)))


def line(index_from, output):
    return f'Fecho-ε(q{index_from}) = {{q{output}}}'
