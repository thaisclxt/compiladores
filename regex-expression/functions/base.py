from classes.state import State
from classes.automaton import Automaton

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
