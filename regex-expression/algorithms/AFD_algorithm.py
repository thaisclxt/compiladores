from classes.fecho_epsilon import FechoEpsilon
from classes.automaton import Automaton
from classes.transition import Transition
from classes.state import State


# Criar um automato finito determinístico a partir de um automato finito não determinístico
def AFD_algorithm(automaton: Automaton, fecho_epsilon: FechoEpsilon) -> None:
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


def convert_to_int(states: list):
    return [int(x[1:]) for x in states]


def map_list(key: int, state_list: list):
    return [x[key] for x in state_list]


def get_alphabet(automaton: Automaton):
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
