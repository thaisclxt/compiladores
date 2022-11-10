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
        print(f'\nAlfabeto:\n--> {{{", ".join(self.alphabet)}}}')

    def show_states(self) -> None:
        output = '\nEstados: '
        # Obs: o estado pode ser inicial e final ao mesmo tempo
        for state in self.states:
            if state == self.initial_state:
                output += '->'
            if state in self.final_states:
                output += '*'
            output += f'q{state.index} '

        print(output)

    def show_transition(self) -> None:
        print('\nTabela de Transição:')
