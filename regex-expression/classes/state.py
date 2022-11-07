class State:
    def __init__(self, index, is_initial: bool, is_final: bool) -> None:
        self.index = index
        self.is_initial = is_initial
        self.is_final = is_final
