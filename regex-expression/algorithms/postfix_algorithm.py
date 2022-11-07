def is_operator(token: str) -> bool:
    return token in '+.*'


def is_operand(token: str) -> bool:
    return not (is_operator(token) or is_parenthesis(token))


def is_parenthesis(token: str) -> bool:
    return token in '()'


def precedence_order(operator: str) -> int:
    return {'(': 0, ')': 0, '+': 1, '.': 2, '*': 3}[operator]


def convert_to_explicit(regular_expression: str) -> str:
    if len(regular_expression) == 1:
        return regular_expression

    actual = regular_expression[0]

    if len(regular_expression) == 2 and actual == '\\':
        return regular_expression

    prox = regular_expression[1]
    resto = regular_expression[1:]

    if is_operand(prox) or prox == '(':
        if (actual != '\\' and is_operand(actual)) or actual == ')' or actual == '*':
            return actual + convert_to_explicit('.' + resto)

    return actual + convert_to_explicit(resto)


def convert_backslash(expression: str, will_remove: bool = True) -> str:
    if will_remove:
        return expression.replace('\\\\', 'ඞ')
    return expression.replace('ඞ', '\\\\')


def postfix_algorithm(regular_expression: str) -> str:
    explicit_expression = list(convert_to_explicit(
        convert_backslash(regular_expression)))

    # Cria a lista de saída postfix e a pilha
    postfix = []
    stack = []

    try:
        # Enquanto a expressão for maior que 0
        while len(explicit_expression) > 0:
            # Remove o primeiro elemento da expressão, para "marcá-lo como lido"
            # e armazena na variável token
            token = explicit_expression.pop(0)

            # Se token for um operando, adiciona na lista de saída
            if is_operand(token):
                postfix.append(token)

                # Se token for \,
                if token == '\\':
                    # Remove o próximo elemento da expressão e armazena na variável prox
                    prox = explicit_expression.pop(0)

                    # Adiciona prox na lista de saída
                    postfix.append(prox)

            # Se token for um parênteses
            elif is_parenthesis(token):

                # Se token for (
                if token == '(':
                    # Adiciona na pilha
                    stack.append(token)

                # Se token for )
                else:
                    # Remove o topo da pilha e adiciona na variável stack_top
                    stack_top = stack.pop()

                    # Enquanto o stack_top for diferente de (, adiciona na lista de saída e vai
                    # desempilhando a pilha e armazenando o retorno na variável stack_top
                    while stack_top != '(':
                        postfix.append(stack_top)
                        stack_top = stack.pop()

            # Se token for um operador
            else:
                # Enquanto a pilha não estiver vazia e a precedencia do topo da pilha for maior
                # ou igual à precedencia do token, adiciona na lista de saída o retorno da remoção
                # do topo da pilha
                while len(stack) > 0 and precedence_order(stack[-1]) >= precedence_order(token):
                    postfix.append(stack.pop())

                # Empilha operador atual
                stack.append(token)
    except:
        return "INVÁLIDA"

    # Enquanto tiver elementos na pilha, vai desempilhando e guardando na variável stack_top
    while len(stack) > 0:
        stack_top = stack.pop()

        # Se o topo da pilha for um operando significa que a expressão é inválida
        if is_operand(stack_top):
            return "INVÁLIDA"

        # Adiciona o topo da pilha na lista de saída
        postfix.append(stack_top)

    return convert_backslash(''.join(postfix), False)
