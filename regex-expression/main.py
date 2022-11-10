from classes.fecho_epsilon import FechoEpsilon
from algorithms.AFD_algorithm import AFD_algorithm
from algorithms.fecho_algorithm import fecho_algorithm
from algorithms.postfix_algorithm import postfix_algorithm
from algorithms.thompson_algorithm import thompson_algorithm


def main() -> None:
    print('Entre com a expressão regular na forma infixa:')
    regular_expression = input('--> ')

    postfix_expression = postfix_algorithm(regular_expression)
    print('\nExpressão pós fixa:\n--> ' + postfix_expression)

    print('\n---------------------------------')

    automaton_result = thompson_algorithm(postfix_expression)
    print('\nAutômato finito não determinístico com movimento vazio:')

    automaton_result.show_alphabet()
    automaton_result.show_states()
    automaton_result.show_transition()

    print('\n---------------------------------')

    print('\nAutômato finito determinístico:')
    fecho_epsilon = FechoEpsilon()

    fecho_algorithm(automaton_result, fecho_epsilon)
    AFD_algorithm(automaton_result, fecho_epsilon)

    print('\n---------------------------------')


if __name__ == '__main__':
    main()
