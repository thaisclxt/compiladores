class FechoEpsilon:
    def __init__(self) -> None:
        self.fecho = dict()

    # Adiciona estados de saída ao fecho no determinado estado de entrada
    def add_output_states(self, input_state: int, output_states: list[str]) -> None:
        self.fecho[input_state] = output_states

    # Converte os estados de saída para inteiro e ordena em ordem crescente
    def order_states(self, index: int) -> None:
        self.fecho[index] = [int(x) for x in self.fecho[index]]
        self.fecho[index].sort()

    # Converte os estados de saída para string precedido de 'q' e retorna o fecho de cada estado
    def fecho_line(self, input_state: int) -> str:
        self.fecho[input_state] = [f"q{x}" for x in self.fecho[input_state]]

        return f'Fecho-ε(q{input_state}) = {{{", ".join(self.fecho[input_state])}}}'
