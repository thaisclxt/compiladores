from classes.state import State


class Transition():
    def __init__(self, symbol: str, from_state: State, to_state: State):
        self.symbol = symbol
        self.from_state = from_state
        self.to_state = to_state
