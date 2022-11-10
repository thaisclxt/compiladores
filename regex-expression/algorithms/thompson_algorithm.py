from classes.AFND import AFND
from functions.base import base
from functions.concatenation import concatenation
from functions.kleene_star import kleene_star
from functions.union import union


def thompson_algorithm(postfix_expression: str) -> AFND:
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
