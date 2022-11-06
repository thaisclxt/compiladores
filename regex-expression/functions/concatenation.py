from classes.state import State
from classes.automaton import Automaton


def concatenation(a: Automaton, b: Automaton):
    # Armazena a quantidade de estados dos automatos
    qtd_a = len(a.states)
    qtd_b = len(b.states)

    # Cria estado inicial e final para o novo automato resultante
    initial_state = State(0, True, False)
    final_state = State(qtd_a + qtd_b - 1, False, True)

    # Cria um novo automato resultante passando o novo estado inicial e final
    automaton = Automaton(initial_state, [final_state])

    # Adiciona o alfabeto ao novo automato resultante
    for letter in a.alphabet:
        automaton.set_alphabet(letter)

    for letter in b.alphabet:
        automaton.set_alphabet(letter)

    # Adiciona o movimento vazio ao alfabeto do novo automato
    automaton.set_alphabet("ε")

    # Cria estados para o novo automato
    automaton.create_state(initial_state)

    for i in range(1, qtd_a + qtd_b - 1):
        automaton.create_state(State(i, False, False))

    automaton.create_state(final_state)

    # Adiciona as transições referente ao automato a
    for t in a.transitions:
        symbol = t.symbol
        index_from = t.from_state.index
        index_to = t.to_state.index

        # from_state recebe o novo estado no index_from e to_state recebe o novo estado no index_to
        from_state = next(x for x in automaton.states if x.index == index_from)
        to_state = next(x for x in automaton.states if x.index == index_to)

        automaton.create_transition(symbol, from_state, to_state)

    # Adiciona as transições referente ao automato b
    for t in b.transitions:
        symbol = t.symbol
        index_from = t.from_state.index
        index_to = t.to_state.index

        # from_state recebe o novo estado no index_from e to_state recebe o novo estado no index_to
        from_state = next(
            x for x in automaton.states if x.index == qtd_a + index_from)
        to_state = next(
            x for x in automaton.states if x.index == qtd_a + index_to)

        automaton.create_transition(symbol, from_state, to_state)

    # Cria uma transição de movimento vazio do antigo final de a para o antigo inicial de b
    old_final_a = next(x for x in automaton.states if x.index == qtd_a - 1)
    old_initial_b = next(x for x in automaton.states if x.index == qtd_a)

    automaton.create_transition('ε', old_final_a, old_initial_b)

    return automaton
