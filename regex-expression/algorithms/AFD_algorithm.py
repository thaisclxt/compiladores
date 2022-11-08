from classes.fecho_epsilon import FechoEpsilon
from classes.automaton import Automaton


def AFD_algorithm(automaton: Automaton, fecho_epsilon: FechoEpsilon) -> None:
    q0 = (convert_to_int(fecho_epsilon.fecho[0]))

    new_alphabet = automaton.alphabet.copy()
    if 'ε' in automaton.alphabet:
        new_alphabet.remove('ε')

    state_list = []
    state_list.append((q0, False))

    print()

    while [x[1] for x in state_list].count(False) != 0:
        for i in range(len(state_list)):
            state, checked = state_list[i]

            print(f'Estado: {state}')
            print(f'Marcado: {checked}\n')

            result = 'Ω'

            for letter in new_alphabet:
                for transition in automaton.transitions:
                    for s in state:
                        if transition.symbol == letter and transition.from_state.index == s:
                            index = transition.to_state.index
                            result = convert_to_int(fecho_epsilon.fecho[index])

                            if result not in [x[0] for x in state_list]:
                                # Adiciona como um estado não marcado
                                state_list.append((result, False))

            if result == 'Ω' and result not in [x[0] for x in state_list]:
                # Adiciona como um estado não marcado
                state_list.append((result, False))

            # Marcar estado
            state_list[i] = (state, True)

    print(state_list)
    print([x[0] for x in state_list])


def convert_to_int(states: list):
    return [int(x[1:]) for x in states]
