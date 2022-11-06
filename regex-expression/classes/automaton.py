from classes.state import State
from classes.transition import Transition


class Automaton():
    def __init__(self, initial_state: State, final_states: list[State]):
        self.initial_state = initial_state
        self.final_states = final_states

        self.alphabet = []
        self.states = []
        self.transitions: list[Transition] = []

    def setAlphabet(self, letter: str):
        if letter not in self.alphabet:
            self.alphabet.append(letter)

    def createState(self, state: State):
        self.states.append(state)

    def createTransition(self, symbol: str, from_state: State, to_state: State):
        self.transitions.append(Transition(symbol, from_state, to_state))

    def showAlphabet(self):
        print('\nAlfabeto:\n--> {' + ', '.join(self.alphabet) + '}')

    def showStates(self):
        output = '\nEstados: '

        for state in self.states:
            if state == self.initial_state:
                output += '->'

            elif state in self.final_states:
                output += '*'

            output += f'q{state.index} '

        print(output)

    def showTransitionTable(self):
        output = ['\nTabela de Transição:']

        for state in self.states:
            if state.is_final:
                continue

            symbol_list = []
            list_index_to = []

            for transition in self.transitions:
                if transition.from_state == state:
                    symbol_list.append(transition.symbol)
                    list_index_to.append(transition.to_state.index)

            output.append(
                self.line(
                    str(state.index),
                    str(transition.symbol),
                    [f'q{x}' for x in list_index_to],
                )
            )

        print("\n".join(output))

    def line(self, index_from, symbol, list_index_to):
        return f'T(q{index_from}, {symbol}) = {{' + ', '.join(list_index_to) + '}'
