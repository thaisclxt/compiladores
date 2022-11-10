from classes.automaton import Automaton


class AFD(Automaton):
    def show_transitions(self) -> None:
        print('\nTabela de Transição:')

        for transition in self.transitions:
            print(
                f'T(q{transition.from_state.index}, {transition.symbol}) = q{transition.to_state.index}')
