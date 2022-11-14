from classes.AFND import AFND
from classes.state import State
from classes.fecho_epsilon import FechoEpsilon


def recursion(input_state: State, automaton: AFND) -> str:
    output_states = f'{input_state.index}'
    for transition in automaton.transitions:
        if transition.from_state == input_state and transition.symbol == 'ε':
            output_states += f' {recursion(transition.to_state, automaton)}'

    return output_states


def fecho_algorithm(automaton: AFND, fecho_epsilon: FechoEpsilon) -> None:
    for state in automaton.states:
        fecho_epsilon.add_output_states(
            state.index, recursion(state, automaton).split(' '))

        fecho_epsilon.order_states(state.index)
        print(fecho_epsilon.fecho_line(state.index))
