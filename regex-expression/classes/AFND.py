from classes.automaton import Automaton


class AFND(Automaton):
    def show_transition(self) -> None:
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

            print(
                f'T(q{state.index}, {symbol_list[0]}) = {{{", ".join([f"q{x}" for x in list_index_to])}}}')
