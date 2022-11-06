from classes.state import State
from classes.automaton import Automaton


def kleene_star(automaton: Automaton):
    # Renomeia os estados
    for state in automaton.states:
        state.index += 1

    # Cria um novo estado inicial e um novo estado final
    new_initial = State(0, True, False)
    new_final = State(len(automaton.states)+1, False, True)

    automaton.create_state(new_initial)
    automaton.create_state(new_final)

    # Adiciona o movimento vazio ao alfabeto do automato
    automaton.set_alphabet("ε")

    # O antigo estado inicial deixa de ser inicial e o antigo final deixa de ser final
    old_initial = automaton.initial_state
    old_final = automaton.final_states[0]

    old_initial.is_initial = False
    old_final.is_final = False

    # Cria as transições entre os estados
    automaton.create_transition('ε', new_initial, old_initial)
    automaton.create_transition('ε', new_initial, new_final)
    automaton.create_transition('ε', old_final, old_initial)
    automaton.create_transition('ε', old_final, new_final)

    return automaton
