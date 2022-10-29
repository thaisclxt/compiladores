from state import State
from automaton import Automaton


def base(symbol: str):
    # Cria um estado inicial e um estado final
    q0 = State(0, True, False)
    qf = State(1, False, True)

    # Cria um automato passando o estado inicial e o estado final
    automaton = Automaton(q0, [qf])

    # Adiciona o alfabeto
    automaton.setAlphabet(symbol)

    # Cria os estados
    automaton.createState(q0)
    automaton.createState(qf)

    # Cria a transição entre os estados
    automaton.createTransition(symbol, q0, qf)

    return automaton


def kleene_star(automaton: Automaton):
    # Renomeia os estados
    for state in automaton.states:
        state.index += 1

    # Cria um novo estado inicial e um novo estado final
    new_initial = State(0, True, False)
    new_final = State(len(automaton.states)+1, False, True)

    automaton.createState(new_initial)
    automaton.createState(new_final)

    # Adiciona o movimento vazio ao alfabeto do automato
    automaton.setAlphabet("&")

    # O antigo estado inicial deixa de ser inicial e o antigo final deixa de ser final
    old_initial = automaton.initial_state
    old_final = automaton.final_states[0]

    old_initial.is_initial = False
    old_final.is_final = False

    # Cria as transições entre os estados
    automaton.createTransition('ε', new_initial, old_initial)
    automaton.createTransition('ε', new_initial, new_final)
    automaton.createTransition('ε', old_final, old_initial)
    automaton.createTransition('ε', old_final, new_final)

    return automaton


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
        automaton.setAlphabet(letter)

    for letter in b.alphabet:
        automaton.setAlphabet(letter)

    # Adiciona o movimento vazio ao alfabeto do novo automato
    automaton.setAlphabet("&")

    # Cria estados para o novo automato
    automaton.createState(initial_state)

    for i in range(1, qtd_a + qtd_b - 1):
        automaton.createState(State(i, False, False))

    automaton.createState(final_state)

    # Adiciona as transições referente ao automato a
    for t in a.transitions:
        symbol = t.symbol
        index_from = t.from_state.index
        index_to = t.to_state.index

        # from_state recebe o novo estado no index_from e to_state recebe o novo estado no index_to
        from_state = next(x for x in automaton.states if x.index == index_from)
        to_state = next(x for x in automaton.states if x.index == index_to)

        automaton.createTransition(symbol, from_state, to_state)

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

        automaton.createTransition(symbol, from_state, to_state)

    # Cria uma transição de movimento vazio do antigo final de a para o antigo inicial de b
    old_final_a = next(x for x in automaton.states if x.index == qtd_a - 1)
    old_initial_b = next(x for x in automaton.states if x.index == qtd_a)

    automaton.createTransition('ε', old_final_a, old_initial_b)

    return automaton


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
    automaton.setAlphabet("&")

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


def thompson_algotithm(postfix_expression: str):
    automaton_list = []

    for element in postfix_expression:
        if element == '*':
            a = automaton_list[-1]
            kleene_star(a)

        elif element == '+':
            a = automaton_list[-2]
            b = automaton_list[-1]

            result = union(a, b)

            automaton_list.pop()
            automaton_list.pop()
            automaton_list.append(result)

        elif element == '.':
            a = automaton_list[-2]
            b = automaton_list[-1]

            result = concatenation(a, b)

            automaton_list.pop()
            automaton_list.pop()
            automaton_list.append(result)

        else:
            automaton_list.append(base(element))

    return automaton_list[-1]


if __name__ == '__main__':
    postfix_expression = 'a*b*.c*+'

    automaton_result = thompson_algotithm(postfix_expression)

    for transition in automaton_result.showTransitions():
        print(transition)
