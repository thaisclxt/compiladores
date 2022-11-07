from classes.state import State
from classes.transition import Transition


class Automaton():
    def __init__(self, initial_state: State, final_states: list[State]) -> None:
        self.initial_state = initial_state
        self.final_states = final_states

        self.alphabet = []
        self.states = []
        self.transitions: list[Transition] = []

    def set_alphabet(self, letter: str) -> None:
        if letter not in self.alphabet:
            self.alphabet.append(letter)

    def create_state(self, state: State) -> None:
        self.states.append(state)

    def create_transition(self, symbol: str, from_state: State, to_state: State) -> None:
        self.transitions.append(Transition(symbol, from_state, to_state))

    def show_alphabet(self) -> None:
        print('\nAlfabeto:\n--> {' + ', '.join(self.alphabet) + '}')

    def show_states(self) -> None:
        output = '\nEstados: '

        for state in self.states:
            if state == self.initial_state:
                output += '->'

            elif state in self.final_states:
                output += '*'

            output += f'q{state.index} '

        print(output)

    def show_transition_table(self) -> None:
        print('\nTabela de Transição:')

        for state in self.states:
            if state.is_final:
                continue

            symbol_list = []
            list_index_to = []

            for transition in self.transitions:
                if transition.from_state == state:
                    symbol_list.append(transition.symbol)
                    list_index_to.append(transition.to_state.index)

            print(self.line(
                str(state.index),
                symbol_list[0],
                [f'q{x}' for x in list_index_to],
            ))

    def line(self, index_from, symbol, list_index_to) -> str:
        return f'T(q{index_from}, {symbol}) = {{' + ', '.join(list_index_to) + '}'
