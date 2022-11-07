from classes.state import State
from classes.automaton import Automaton


def base(symbol: str) -> Automaton:
    # Cria um estado inicial e um estado final
    q0 = State(0, True, False)
    qf = State(1, False, True)

    # Cria um automato passando o estado inicial e o estado final
    automaton = Automaton(q0, [qf])

    # Adiciona o alfabeto
    automaton.set_alphabet(symbol)

    # Cria os estados
    automaton.create_state(q0)
    automaton.create_state(qf)

    # Cria a transição entre os estados
    automaton.create_transition(symbol, q0, qf)

    return automaton
