from postfix import convert_to_postfix
from thompson_algorithm import thompson_algorithm


def main():
    print('Entre com a expressão regular na forma infixa:')
    regular_expression = input('--> ')

    postfix_expression = convert_to_postfix(regular_expression)
    print('\nExpressão pós fixa:\n--> ' + postfix_expression)

    automaton_result = thompson_algorithm(postfix_expression)
    print('\n-----------------------\n')
    print('AFND-ɛ:\n')
    for transition in automaton_result.showTransitions():
        print(transition)


if __name__ == '__main__':
    main()
