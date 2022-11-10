from classes.fecho_epsilon import FechoEpsilon
from classes.transition import Transition
from classes.state import State
from classes.AFND import AFND
from classes.AFD import AFD


# Criar um automato finito determinístico a partir de um automato finito não determinístico
def AFD_algorithm(automaton: AFND, fecho_epsilon: FechoEpsilon) -> None:
    # Lista de estados do AFD que armazena uma tupla como uma lista de inteiros e um booleano para indicar se é um estado marcado
    state_list = []

    # Lista de transições do AFD
    transition_list = []

    # Index do estado inicial do AFND
    AFND_q0 = automaton.initial_state.index

    # O estado inicial do AFD recebe o resultado do fecho de q0 convertido em uma lista de inteiros
    AFD_q0 = convert_to_int(fecho_epsilon.fecho[AFND_q0])

    # Adiciona o estado inicial à lista de estados como não marcado
    state_list.append((AFD_q0, False))

    # Pegar o alfabeto de AFD excluindo 'ε' caso exista
    alphabet = get_alphabet(automaton)

    # Enquanto houver algum estado marcado
    while map_list(1, state_list).count(False) != 0:
        # Para cada estado na lista de estados do AFD
        for i in range(len(state_list)):
            state, checked = state_list[i]
            # Se o estado já está marcado, olhe o próximo estado
            if checked:
                continue

            # Para cada letra no alfabeto do AFD
            for letter in alphabet:
                # Resultado inicialmente recebe fi
                result = ['Φ']

                # Para cada transição do AFND
                for transition in automaton.transitions:
                    # Se não encontrar transição ir para a proxima
                    if transition.symbol != letter or transition.from_state.index not in state:
                        continue

                    # Escopo principal do algoritmo
                    result = get_result(transition, fecho_epsilon, result)

                # Se o resultado não estiver na lista de estados prontos, adiciona como um estado não marcado
                if result not in map_list(0, state_list):
                    state_list.append((result, False))

                transition_list.append((state, letter, result))

            # Marca o estado
            state_list[i] = (state, True)

    # Imprimir transições
    for transition in transition_list:
        print(
            f'T({convert_to_str(transition[0])}, {convert_to_str(transition[1])})={convert_to_str(transition[2])}')

    new_automaton(state_list, automaton, AFD_q0, transition_list, alphabet)


def convert_to_int(states: list):
    return [int(x[1:]) for x in states]


def map_list(key: int, state_list: list):
    return [x[key] for x in state_list]


def get_alphabet(automaton: AFND):
    AFD_alphabet = automaton.alphabet.copy()
    if 'ε' in automaton.alphabet:
        AFD_alphabet.remove('ε')
    return AFD_alphabet


def get_result(transition: Transition, fecho_epsilon: FechoEpsilon, result: list):
    to_state = transition.to_state.index

    # Novo resultado recebe o retorno do fecho de to_state convertido em uma lista de inteiros
    new_result = convert_to_int(fecho_epsilon.fecho[to_state])

    # Se o resultado não for fi, irá concatenar com o novo resultado
    return new_result if result == ['Φ'] else [*result, *new_result]


def convert_to_str(list: list):
    return ", ".join([str(x) for x in list])


def get_initial_state(state_list: list, AFD_q0: int):
    return state_list[0]


def get_final_state(old_state_list: list, automaton: AFND, state_list: list):
    final_states_index = []

    AFND_qf = [x.index for x in automaton.final_states]
    # Para cada index de estado no conjunto de estados finais
    for final_state_index in AFND_qf:
        for x in map_list(0, old_state_list):
            if final_state_index in x:
                final_states_index.append(old_state_list.index((x, True)))

    for y in final_states_index:
        for w in state_list:
            if y == w.index:
                w.is_final = True

    return [x for x in state_list if x.is_final]


def new_automaton(state_list: list, automaton: AFND, AFD_q0: int, transition_list: list, alphabet):
    lista_de_estados_do_afd = []
    for state in map_list(0, state_list):
        lista_de_estados_do_afd.append(
            State(state_list.index((state, True)), False, False))

    initial_state = get_initial_state(lista_de_estados_do_afd, AFD_q0)
    initial_state.is_initial = True

    final_state_list = get_final_state(
        state_list, automaton, lista_de_estados_do_afd)

    new_automaton = AFD(initial_state, final_state_list)
    new_automaton.alphabet = alphabet
    new_automaton.states = lista_de_estados_do_afd

    print()
    for transition in transition_list:
        # f'T({convert_to_str(transition[0])}, {convert_to_str(transition[1])})={convert_to_str(transition[2])}')
        symbol = convert_to_str(transition[1])

        for x in lista_de_estados_do_afd:
            if state_list.index((transition[0], True)) == x.index:
                from_state = x

            elif state_list.index((transition[2], True)) == x.index:
                to_state = x
        new_automaton.create_transition(symbol, from_state, to_state)

    new_automaton.show_alphabet()
    new_automaton.show_states()
    new_automaton.show_transitions()
