from classes.state import State
from classes.automaton import Automaton


# Quem é inicial deixa de ser inicial e quem é final deixa de ser final
def union(a: Automaton, b: Automaton):
    # Armazena a quantidade de estados dos automatos
    qtd_a = len(a.states)
    qtd_b = len(b.states)

    # Cria estado inicial e final
    new_initial = State(0, True, False)
    new_final = State(qtd_a + qtd_b + 1, False, True)

    # Cria um novo automato resultante passando o novo estado inicial e final
    automaton = Automaton(new_initial, [new_final])

    # Adiciona o alfabeto ao novo automato resultante
    for letter in a.alphabet:
        automaton.setAlphabet(letter)

    for letter in b.alphabet:
        automaton.setAlphabet(letter)

    # Adiciona o movimento vazio ao alfabeto do novo automato
    automaton.setAlphabet("ε")

    # Cria os estados do novo automato resultante
    automaton.createState(new_initial)

    for i in range(1, qtd_a + qtd_b + 1):
        automaton.createState(State(i, False, False))

    automaton.createState(new_final)

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

        automaton.createTransition(symbol, from_state, to_state)

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

        automaton.createTransition(symbol, from_state, to_state)

    # Pega os antigos estados iniciais e finais
    initial_a = next(x for x in automaton.states if x.index == 1)
    initial_b = next(x for x in automaton.states if x.index == qtd_a + 1)

    final_a = next(x for x in automaton.states if x.index == qtd_a)
    final_b = next(x for x in automaton.states if x.index == qtd_a + qtd_b)

    # Adiciona as novas transições de movimento vazio
    automaton.createTransition('ε', new_initial, initial_a)
    automaton.createTransition('ε', new_initial, initial_b)
    automaton.createTransition('ε', final_a, new_final)
    automaton.createTransition('ε', final_b, new_final)

    return automaton
