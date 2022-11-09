from classes.fecho_epsilon import FechoEpsilon
from classes.automaton import Automaton
from classes.transition import Transition
from classes.state import State


def AFD_algorithm(automaton: Automaton, fecho_epsilon: FechoEpsilon) -> None:
    q0 = (convert_to_int(fecho_epsilon.fecho[0]))

    new_alphabet = automaton.alphabet.copy()
    if 'ε' in automaton.alphabet:
        new_alphabet.remove('ε')

    state_list = []
    transition_list = []
    state_list.append((q0, False))

    print()

    while [x[1] for x in state_list].count(False) != 0:
        for i in range(len(state_list)):
            state, checked = state_list[i]
            if checked:
                continue

            for letter in new_alphabet:
                result = ['Ω']
                for transition in automaton.transitions:
                    if transition.symbol != letter or transition.from_state.index not in state:
                        continue

                    to_state = transition.to_state.index
                    new_result = convert_to_int(fecho_epsilon.fecho[to_state])
                    result = new_result if result == ['Ω'] else [
                        *result, *new_result]

                    print(f'Transição de {state_list[i][0]}', end='')
                    print(f' para {result} com simbolo {letter}')

                if result not in [x[0] for x in state_list]:
                    # Adiciona como um estado não marcado
                    state_list.append((result, False))

                transition_list.append((state, letter, result))

            # Marcar estado
            state_list[i] = (state, True)

    print(state_list)
    print(transition_list)


def convert_to_int(states: list):
    return [int(x[1:]) for x in states]


def get_result():
    pass
