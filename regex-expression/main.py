from functions.fecho_e import fecho_algorithm
from postfix import convert_to_postfix
from thompson_algorithm import thompson_algorithm


def main():
    print('Entre com a expressão regular na forma infixa:')
    regular_expression = input('--> ')

    postfix_expression = convert_to_postfix(regular_expression)
    print('\nExpressão pós fixa:\n--> ' + postfix_expression)

    print('\n---------------------------------')

    automaton_result = thompson_algorithm(postfix_expression)
    print('\nAutômato finito não determinístico com movimento vazio:')

    automaton_result.showAlphabet()
    automaton_result.showStates()
    automaton_result.showTransitionTable()

    print('\n---------------------------------')

    print('\nAutômato finito determinístico:')
    fecho_algorithm(automaton_result)


if __name__ == '__main__':
    main()
