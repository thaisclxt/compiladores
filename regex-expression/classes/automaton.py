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

    def showTransitions(self):
        output = []

        for transition in self.transitions:
            output.append('T(q' + str(transition.from_state.index) +
                          ', ' + transition.symbol +
                          ') = {q' + str(transition.to_state.index) + '}')
        return output
