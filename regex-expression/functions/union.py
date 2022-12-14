from classes.state import State
from classes.AFND import AFND


# Quem é inicial deixa de ser inicial e quem é final deixa de ser final
def union(a: AFND, b: AFND) -> AFND:
    # Armazena a quantidade de estados dos automatos
    qtd_a = len(a.states)
    qtd_b = len(b.states)

    # Cria estado inicial e final
    new_initial = State(0, True, False)
    new_final = State(qtd_a + qtd_b + 1, False, True)

    # Cria um novo automato resultante passando o novo estado inicial e final
    automaton = AFND(new_initial, [new_final])

    # Adiciona o alfabeto ao novo automato resultante
    for letter in a.alphabet:
        automaton.set_alphabet(letter)

    for letter in b.alphabet:
        automaton.set_alphabet(letter)

    # Adiciona o movimento vazio ao alfabeto do novo automato
    automaton.set_alphabet("ε")

    # Cria os estados do novo automato resultante
    automaton.create_state(new_initial)

    for i in range(1, qtd_a + qtd_b + 1):
        automaton.create_state(State(i, False, False))

    automaton.create_state(new_final)

    # Adiciona as transições referente ao automato a
    for t in a.transitions:
        symbol = t.symbol
        index_from = t.from_state.index
        index_to = t.to_state.index

        # from_state recebe o novo estado no index_from e to_state recebe o novo estado no index_to
        from_state = next(
            x for x in automaton.states if x.index == index_from + 1)
        to_state = next(
            x for x in automaton.states if x.index == index_to + 1)

        automaton.create_transition(symbol, from_state, to_state)

    # Adiciona as transições referente ao automato b
    for t in b.transitions:
        symbol = t.symbol
        index_from = t.from_state.index
        index_to = t.to_state.index

        # from_state recebe o novo estado no index_from e to_state recebe o novo estado no index_to
        from_state = next(
            x for x in automaton.states if x.index == qtd_a + index_from + 1)
        to_state = next(
            x for x in automaton.states if x.index == qtd_a + index_to + 1)

        automaton.create_transition(symbol, from_state, to_state)

    # Pega os antigos estados iniciais e finais
    initial_a = next(x for x in automaton.states if x.index == 1)
    initial_b = next(x for x in automaton.states if x.index == qtd_a + 1)

    final_a = next(x for x in automaton.states if x.index == qtd_a)
    final_b = next(x for x in automaton.states if x.index == qtd_a + qtd_b)

    # Adiciona as novas transições de movimento vazio
    automaton.create_transition('ε', new_initial, initial_a)
    automaton.create_transition('ε', new_initial, initial_b)
    automaton.create_transition('ε', final_a, new_final)
    automaton.create_transition('ε', final_b, new_final)

    return automaton
